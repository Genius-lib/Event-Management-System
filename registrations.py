"""Event registration, capacity checking and payment tracking."""
from datetime import date
from storage import read_data, add_record, save_data
from helpers import make_id, ask_text, print_table

def register_attendee():
    events = read_data("events")
    attendees = read_data("attendees")
    registrations = read_data("registrations")
    print("\nEVENTS")
    print_table(events, [("event_id", "ID"), ("event_name", "EVENT"),
                         ("event_date", "DATE"), ("capacity", "CAPACITY"),
                         ("status", "STATUS")])
    event_id = ask_text("Enter event ID: ").upper()
    event = next((item for item in events if item["event_id"] == event_id), None)
    if event is None or event["status"] != "Scheduled":
        print("Event not found or event is not open for registration.")
        return
    active_count = len([item for item in registrations
                        if item["event_id"] == event_id and item["status"] == "Active"])
    if active_count >= int(event["capacity"]):
        print("Registration is closed because the event is full.")
        return

    print("\nATTENDEES")
    print_table(attendees, [("attendee_id", "ID"), ("full_name", "NAME"),
                            ("phone", "PHONE"), ("email", "EMAIL")])
    attendee_id = ask_text("Enter attendee ID: ").upper()
    attendee = next((item for item in attendees if item["attendee_id"] == attendee_id), None)
    if attendee is None:
        print("Attendee not found.")
        return

    for item in registrations:
        if (item["event_id"] == event_id and item["attendee_id"] == attendee_id
                and item["status"] == "Active"):
            print("This attendee is already registered for this event.")
            return

    while True:
        try:
            fee = float(input("Registration fee (enter 0 if free): "))
            if fee >= 0:
                break
            print("Fee cannot be negative.")
        except ValueError:
            print("Enter a valid number.")
    if fee == 0:
        payment_status = "Paid"
    else:
        payment_status = input("Payment status (Paid/Unpaid): ").strip().capitalize()
        while payment_status not in ["Paid", "Unpaid"]:
            payment_status = input("Enter Paid or Unpaid: ").strip().capitalize()

    registration = {
        "registration_id": make_id(registrations, "registration_id", "REG"),
        "attendee_id": attendee_id,
        "event_id": event_id,
        "registration_date": str(date.today()),
        "fee": str(round(fee, 2)),
        "payment_status": payment_status,
        "status": "Active"
    }
    add_record("registrations", registration)
    print("Registration successful. Registration ID:", registration["registration_id"])

def view_event_attendees():
    event_id = ask_text("Enter event ID: ").upper()
    event = next((item for item in read_data("events") if item["event_id"] == event_id), None)
    if event is None:
        print("Event not found.")
        return
    registrations = [item for item in read_data("registrations")
                     if item["event_id"] == event_id and item["status"] == "Active"]
    attendees = read_data("attendees")
    rows = []
    for registration in registrations:
        person = next((item for item in attendees
                       if item["attendee_id"] == registration["attendee_id"]), None)
        if person:
            rows.append({
                "registration_id": registration["registration_id"],
                "full_name": person["full_name"],
                "phone": person["phone"],
                "payment_status": registration["payment_status"]
            })
    print("\nATTENDEES FOR:", event["event_name"])
    print_table(rows, [("registration_id", "REG ID"), ("full_name", "ATTENDEE"),
                       ("phone", "PHONE"), ("payment_status", "PAYMENT")])
    remaining = int(event["capacity"]) - len(registrations)
    print("Registered:", len(registrations))
    print("Remaining places:", remaining)

def update_registration():
    registrations = read_data("registrations")
    print_table(registrations, [("registration_id", "REG ID"), ("attendee_id", "ATTENDEE"),
                                ("event_id", "EVENT"), ("fee", "FEE"),
                                ("payment_status", "PAYMENT"), ("status", "STATUS")])
    reg_id = ask_text("Enter registration ID: ").upper()
    registration = next((item for item in registrations
                         if item["registration_id"] == reg_id), None)
    if registration is None:
        print("Registration not found.")
        return
    print("1. Mark as Paid")
    print("2. Mark as Unpaid")
    print("3. Cancel registration")
    choice = input("Choose: ").strip()
    if choice == "1":
        registration["payment_status"] = "Paid"
    elif choice == "2":
        registration["payment_status"] = "Unpaid"
    elif choice == "3":
        registration["status"] = "Cancelled"
    else:
        print("Invalid choice.")
        return
    save_data("registrations", registrations)
    print("Registration updated.")

def registration_menu():
    while True:
        print("\nREGISTRATION MANAGEMENT")
        print("1. Register attendee for an event")
        print("2. View attendees for an event")
        print("3. Update payment / cancel registration")
        print("0. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            register_attendee()
        elif choice == "2":
            view_event_attendees()
        elif choice == "3":
            update_registration()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
