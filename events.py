"""Event management functions."""
from datetime import datetime
from storage import read_data, add_record, save_data
from helpers import make_id, ask_text, ask_positive_number, ask_date, ask_time, print_table

def get_venue_name(venue_id):
    for venue in read_data("venues"):
        if venue["venue_id"] == venue_id:
            return venue["venue_name"]
    return "Unknown venue"

def count_active_registrations(event_id):
    return len([row for row in read_data("registrations")
                if row["event_id"] == event_id and row["status"] == "Active"])

def view_events():
    events = sorted(read_data("events"), key=lambda item: item["event_date"])
    for event in events:
        event["venue_name"] = get_venue_name(event["venue_id"])
    print_table(events, [("event_id", "ID"), ("event_name", "EVENT"),
                         ("event_date", "DATE"), ("event_time", "TIME"),
                         ("venue_name", "VENUE"), ("capacity", "CAPACITY"),
                         ("status", "STATUS")])

def create_event():
    print("\nCREATE A NEW EVENT")
    venues = read_data("venues")
    if not venues:
        print("There are no venues. Add a venue first.")
        return
    print_table(venues, [("venue_id", "ID"), ("venue_name", "VENUE"),
                         ("location", "LOCATION"), ("capacity", "CAPACITY")])
    venue_id = ask_text("Enter venue ID: ").upper()
    venue = next((item for item in venues if item["venue_id"] == venue_id), None)
    if venue is None:
        print("Venue ID was not found.")
        return
    name = ask_text("Event name: ")
    event_date = ask_date("Event date")
    event_time = ask_time("Event time")
    capacity = ask_positive_number("Event capacity: ")
    if capacity > int(venue["capacity"]):
        print("Event capacity cannot be greater than venue capacity.")
        return
    events = read_data("events")
    event = {
        "event_id": make_id(events, "event_id", "EVT"),
        "event_name": name,
        "event_date": event_date,
        "event_time": event_time,
        "venue_id": venue_id,
        "capacity": str(capacity),
        "status": "Scheduled"
    }
    add_record("events", event)
    print("Event created. Event ID:", event["event_id"])

def search_event():
    search = input("Enter event ID or part of event name: ").strip().lower()
    found = [event for event in read_data("events")
             if search in event["event_id"].lower()
             or search in event["event_name"].lower()]
    for event in found:
        event["venue_name"] = get_venue_name(event["venue_id"])
    print_table(found, [("event_id", "ID"), ("event_name", "EVENT"),
                        ("event_date", "DATE"), ("event_time", "TIME"),
                        ("venue_name", "VENUE"), ("status", "STATUS")])

def update_event():
    events = read_data("events")
    view_events()
    event_id = ask_text("Enter event ID to update: ").upper()
    event = next((item for item in events if item["event_id"] == event_id), None)
    if event is None:
        print("Event not found.")
        return
    print("Leave a field blank to keep the current value.")
    new_name = input("New event name [" + event["event_name"] + "]: ").strip()
    new_date = input("New date [" + event["event_date"] + "] (YYYY-MM-DD): ").strip()
    new_time = input("New time [" + event["event_time"] + "] (HH:MM): ").strip()
    new_capacity = input("New capacity [" + event["capacity"] + "]: ").strip()

    if new_name:
        event["event_name"] = new_name
    if new_date:
        try:
            datetime.strptime(new_date, "%Y-%m-%d")
            event["event_date"] = new_date
        except ValueError:
            print("Invalid date. Update cancelled.")
            return
    if new_time:
        try:
            datetime.strptime(new_time, "%H:%M")
            event["event_time"] = new_time
        except ValueError:
            print("Invalid time. Update cancelled.")
            return
    if new_capacity:
        try:
            capacity = int(new_capacity)
            venue = next(v for v in read_data("venues") if v["venue_id"] == event["venue_id"])
            if capacity <= 0 or capacity > int(venue["capacity"]):
                print("Capacity must be positive and not exceed venue capacity.")
                return
            if capacity < count_active_registrations(event_id):
                print("Capacity cannot be below the number already registered.")
                return
            event["capacity"] = str(capacity)
        except ValueError:
            print("Capacity must be a whole number.")
            return
    save_data("events", events)
    print("Event updated successfully.")

def cancel_event():
    events = read_data("events")
    view_events()
    event_id = ask_text("Enter event ID to cancel: ").upper()
    event = next((item for item in events if item["event_id"] == event_id), None)
    if event is None:
        print("Event not found.")
        return
    confirm = input("Type YES to confirm cancellation: ").strip().upper()
    if confirm == "YES":
        event["status"] = "Cancelled"
        save_data("events", events)
        registrations = read_data("registrations")
        for registration in registrations:
            if registration["event_id"] == event_id and registration["status"] == "Active":
                registration["status"] = "Cancelled"
        save_data("registrations", registrations)
        print("Event cancelled.")
    else:
        print("Cancellation stopped.")

def event_menu():
    while True:
        print("\nEVENT MANAGEMENT")
        print("1. View events")
        print("2. Create event")
        print("3. Search event")
        print("4. Update event")
        print("5. Cancel event")
        print("0. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            view_events()
        elif choice == "2":
            create_event()
        elif choice == "3":
            search_event()
        elif choice == "4":
            update_event()
        elif choice == "5":
            cancel_event()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
