"""Attendee registration and viewing functions."""
from storage import read_data, add_record
from helpers import make_id, ask_text, print_table

def view_attendees():
    attendees = read_data("attendees")
    print_table(attendees, [("attendee_id", "ID"), ("full_name", "FULL NAME"),
                            ("phone", "PHONE"), ("email", "EMAIL")])

def add_attendee():
    print("\nREGISTER A NEW ATTENDEE")
    name = ask_text("Full name: ")
    phone = ask_text("Phone number: ")
    email = ask_text("Email address: ")
    attendees = read_data("attendees")
    attendee = {
        "attendee_id": make_id(attendees, "attendee_id", "ATT"),
        "full_name": name,
        "phone": phone,
        "email": email
    }
    add_record("attendees", attendee)
    print("Attendee registered. Attendee ID:", attendee["attendee_id"])

def search_attendee():
    search = input("Enter attendee ID or part of name: ").strip().lower()
    found = [person for person in read_data("attendees")
             if search in person["attendee_id"].lower()
             or search in person["full_name"].lower()]
    print_table(found, [("attendee_id", "ID"), ("full_name", "FULL NAME"),
                        ("phone", "PHONE"), ("email", "EMAIL")])

def attendee_menu():
    while True:
        print("\nATTENDEE MANAGEMENT")
        print("1. View attendees")
        print("2. Register attendee")
        print("3. Search attendee")
        print("0. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            view_attendees()
        elif choice == "2":
            add_attendee()
        elif choice == "3":
            search_attendee()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
