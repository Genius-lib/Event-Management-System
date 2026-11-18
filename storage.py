"""Functions for creating and working with the CSV data files."""
import csv
import os

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data")

HEADERS = {
    "events": ["event_id", "event_name", "event_date", "event_time", "venue_id", "capacity", "status"],
    "venues": ["venue_id", "venue_name", "location", "capacity"],
    "attendees": ["attendee_id", "full_name", "phone", "email"],
    "registrations": ["registration_id", "attendee_id", "event_id", "registration_date", "fee", "payment_status", "status"]
}

def create_files():
    """Create the data folder and CSV files with headings if they do not exist."""
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    for table, headings in HEADERS.items():
        path = os.path.join(DATA_FOLDER, table + ".csv")
        if not os.path.exists(path):
            with open(path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(headings)

def read_data(table):
    """Read all rows from a CSV file and return them as a list of dictionaries."""
    create_files()
    path = os.path.join(DATA_FOLDER, table + ".csv")
    with open(path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_data(table, records):
    """Replace a CSV file's contents with the records supplied."""
    create_files()
    path = os.path.join(DATA_FOLDER, table + ".csv")
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS[table])
        writer.writeheader()
        writer.writerows(records)

def add_record(table, record):
    """Add one new record to the end of a CSV file."""
    create_files()
    path = os.path.join(DATA_FOLDER, table + ".csv")
    with open(path, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS[table])
        writer.writerow(record)

def load_sample_data():
    """Load a small sample dataset only when all four CSV files are empty."""
    if any(read_data(name) for name in HEADERS):
        return

    venues = [
        ["VEN001", "Samuel Kanyon Doe Sports Complex", "Paynesville, Montserrado", "30000"],
        ["VEN002", "The Executive Pavilion", "Ashmun Street, Monrovia", "1000"],
        ["VEN003", "Centennial Memorial Pavilion", "Ashmun Street, Monrovia", "1000"],
        ["VEN004", "Antoinette Tubman Stadium", "Central Monrovia", "8000"],
        ["VEN005", "Sinkor Palace Hotel", "Tubman Boulevard, Monrovia", "300"],
        ["VEN006", "Riverside Beach", "Monrovia", "500"],
        ["VEN007", "Liberian Learning Center", "Monrovia", "250"],
        ["VEN008", "Ministerial Complex", "Congo Town, Monrovia", "1500"],
        ["VEN009", "Hotel Africa", "Virginia, Montserrado", "500"],
        ["VEN010", "Ariana Bar and Restaurant", "Monrovia", "200"]
    ]
    for row in venues:
        add_record("venues", dict(zip(HEADERS["venues"], row)))

    events = [
        ["EVT001", "National County Sports Meet - Opening", "2026-11-28", "10:00", "VEN001", "25000", "Scheduled"],
        ["EVT002", "Orange 5G Fest", "2026-11-22", "10:00", "VEN001", "5000", "Scheduled"],
        ["EVT003", "Liberia National Food Festival (LINFFEST)", "2026-11-26", "10:00", "VEN005", "250", "Scheduled"],
        ["EVT004", "Monrovia Fest", "2026-11-29", "10:00", "VEN001", "7000", "Scheduled"],
        ["EVT005", "MTN Liberia Music Awards", "2026-12-05", "18:00", "VEN008", "1200", "Scheduled"],
        ["EVT006", "King Caro Concert - Stay in School", "2026-12-04", "18:00", "VEN006", "450", "Scheduled"],
        ["EVT007", "Liberia Book Festival", "2026-12-12", "09:00", "VEN007", "200", "Scheduled"],
        ["EVT008", "DRIP FEST", "2026-12-18", "18:00", "VEN009", "450", "Scheduled"],
        ["EVT009", "National County Sports Meet - Grand Final", "2026-12-27", "10:00", "VEN001", "25000", "Scheduled"],
        ["EVT010", "179th National Flag Day Celebration", "2026-08-24", "09:00", "VEN002", "900", "Completed"]
    ]
    for row in events:
        add_record("events", dict(zip(HEADERS["events"], row)))

    attendees = [
        ["ATT001", "Mary Johnson", "0777000001", "mary@example.com"],
        ["ATT002", "James Kollie", "0888000002", "james@example.com"],
        ["ATT003", "Sarah Doe", "0777000003", "sarah@example.com"],
        ["ATT004", "Peter Williams", "0888000004", "peter@example.com"],
        ["ATT005", "Grace Cooper", "0777000005", "grace@example.com"]
    ]
    for row in attendees:
        add_record("attendees", dict(zip(HEADERS["attendees"], row)))

    registrations = [
        ["REG001", "ATT001", "EVT001", "2026-11-10", "10.00", "Paid", "Active"],
        ["REG002", "ATT002", "EVT001", "2026-11-11", "10.00", "Unpaid", "Active"],
        ["REG003", "ATT003", "EVT003", "2026-11-12", "5.00", "Paid", "Active"],
        ["REG004", "ATT004", "EVT004", "2026-11-13", "15.00", "Unpaid", "Active"],
        ["REG005", "ATT005", "EVT007", "2026-11-14", "0.00", "Paid", "Active"]
    ]
    for row in registrations:
        add_record("registrations", dict(zip(HEADERS["registrations"], row)))
