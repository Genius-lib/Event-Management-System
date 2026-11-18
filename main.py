"""Main file: starts the Event Management System and displays its main menu."""
from storage import create_files, load_sample_data
from events import event_menu, view_events
from venues import venue_menu
from attendees import attendee_menu
from registrations import registration_menu
from reports import report_menu
from helpers import show_heading, pause

def main():
    create_files()
    load_sample_data()

    while True:
        show_heading("MAIN MENU")
        print("1. Event Management")
        print("2. Venue Management")
        print("3. Attendee Management")
        print("4. Registration Management")
        print("5. Reports")
        print("6. View All Events")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            event_menu()
        elif choice == "2":
            venue_menu()
        elif choice == "3":
            attendee_menu()
        elif choice == "4":
            registration_menu()
        elif choice == "5":
            report_menu()
        elif choice == "6":
            view_events()
            pause()
        elif choice == "0":
            print("\nThank you for using the Event Management System.")
            break
        else:
            print("\nInvalid choice. Please select 0 to 6.")
            pause()

if __name__ == "__main__":
    main()
