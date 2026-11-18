"""Venue management functions."""
from storage import read_data, add_record
from helpers import make_id, ask_text, ask_positive_number, print_table

def view_venues():
    venues = read_data("venues")
    print_table(venues, [("venue_id", "ID"), ("venue_name", "VENUE"),
                         ("location", "LOCATION"), ("capacity", "CAPACITY")])

def add_venue():
    print("\nADD A NEW VENUE")
    name = ask_text("Venue name: ")
    location = ask_text("Venue location: ")
    capacity = ask_positive_number("Venue capacity: ")
    venues = read_data("venues")
    venue = {
        "venue_id": make_id(venues, "venue_id", "VEN"),
        "venue_name": name,
        "location": location,
        "capacity": str(capacity)
    }
    add_record("venues", venue)
    print("Venue added. Venue ID:", venue["venue_id"])

def update_venue():
    venues = read_data("venues")
    view_venues()
    venue_id = ask_text("Enter venue ID to update: ").upper()
    venue = next((item for item in venues if item["venue_id"] == venue_id), None)
    if venue is None:
        print("Venue not found.")
        return

    print("Leave a field blank to keep its current value.")
    new_name = input("New venue name [" + venue["venue_name"] + "]: ").strip()
    new_location = input("New location [" + venue["location"] + "]: ").strip()
    new_capacity = input("New capacity [" + venue["capacity"] + "]: ").strip()

    if new_capacity:
        try:
            capacity = int(new_capacity)
            if capacity <= 0:
                print("Venue capacity must be greater than zero.")
                return
            events = read_data("events")
            for event in events:
                if event["venue_id"] == venue_id and int(event["capacity"]) > capacity:
                    print("Cannot reduce venue capacity below an existing event's capacity.")
                    return
            venue["capacity"] = str(capacity)
        except ValueError:
            print("Capacity must be a whole number.")
            return

    if new_name:
        venue["venue_name"] = new_name
    if new_location:
        venue["location"] = new_location

    from storage import save_data
    save_data("venues", venues)
    print("Venue updated successfully.")

def venue_menu():
    while True:
        print("\nVENUE MANAGEMENT")
        print("1. View venues")
        print("2. Add venue")
        print("3. Update venue")
        print("0. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            view_venues()
        elif choice == "2":
            add_venue()
        elif choice == "3":
            update_venue()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
