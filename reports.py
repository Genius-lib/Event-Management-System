"""Simple reports required by the project."""
from storage import read_data
from helpers import print_table

def event_report():
    events = sorted(read_data("events"), key=lambda item: item["event_date"])
    registrations = read_data("registrations")
    rows = []
    for event in events:
        count = len([item for item in registrations
                     if item["event_id"] == event["event_id"] and item["status"] == "Active"])
        rows.append({
            "event_name": event["event_name"],
            "event_date": event["event_date"],
            "capacity": event["capacity"],
            "registered": count,
            "remaining": int(event["capacity"]) - count
        })
    print_table(rows, [("event_name", "EVENT"), ("event_date", "DATE"),
                       ("capacity", "CAPACITY"), ("registered", "REGISTERED"),
                       ("remaining", "PLACES LEFT")])

def payment_report():
    registrations = [item for item in read_data("registrations")
                     if item["status"] == "Active"]
    paid = [item for item in registrations if item["payment_status"] == "Paid"]
    unpaid = [item for item in registrations if item["payment_status"] == "Unpaid"]
    paid_total = sum(float(item["fee"]) for item in paid)
    unpaid_total = sum(float(item["fee"]) for item in unpaid)
    print("\nPAYMENT REPORT")
    print("Active registrations:", len(registrations))
    print("Paid:", len(paid), "| Total paid: $", format(paid_total, ".2f"))
    print("Unpaid:", len(unpaid), "| Outstanding: $", format(unpaid_total, ".2f"))

def report_menu():
    while True:
        print("\nREPORTS")
        print("1. Event attendance and remaining places")
        print("2. Payment summary")
        print("0. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            event_report()
        elif choice == "2":
            payment_report()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
