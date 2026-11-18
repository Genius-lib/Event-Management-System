"""Simple input validation and display functions used by the program."""
from datetime import datetime

def show_heading(title):
    print("\n" + "=" * 60)
    print("EVENT MANAGEMENT SYSTEM")
    print(title.upper())
    print("=" * 60)

def pause():
    input("\nPress ENTER to continue...")

def ask_text(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("This field cannot be empty.")

def ask_positive_number(message):
    while True:
        try:
            number = int(input(message))
            if number > 0:
                return number
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a whole number.")

def ask_date(message):
    while True:
        value = input(message + " (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Invalid date. Example: 2026-11-28")

def ask_time(message):
    while True:
        value = input(message + " (HH:MM): ").strip()
        try:
            datetime.strptime(value, "%H:%M")
            return value
        except ValueError:
            print("Invalid time. Example: 14:30")

def make_id(records, field, prefix):
    highest = 0
    for record in records:
        try:
            number = int(record[field].replace(prefix, ""))
            highest = max(highest, number)
        except (ValueError, KeyError):
            pass
    return prefix + str(highest + 1).zfill(3)

def print_table(records, fields):
    if not records:
        print("\nNo records found.")
        return
    headings = [heading for key, heading in fields]
    widths = []
    for index, (key, heading) in enumerate(fields):
        widest = max([len(heading)] + [len(str(row.get(key, ""))) for row in records])
        widths.append(widest)
    print("\n" + " | ".join(headings[i].ljust(widths[i]) for i in range(len(fields))))
    print("-+-".join("-" * width for width in widths))
    for row in records:
        print(" | ".join(str(row.get(key, "")).ljust(widths[i])
                         for i, (key, heading) in enumerate(fields)))
