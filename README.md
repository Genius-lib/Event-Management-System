# Event Management System

**Course project:** Python 3 Console Application  
**Storage:** CSV files using Python's built-in `csv` module  
**Interface:** Text-based console menu

## 1. Project purpose

The Event Management System helps an event organizer keep basic records of events, venues, attendees and event registrations. It also records whether a registration fee has been paid.

## 2. Requirements from the assignment that this project follows

| Teacher's requirement | How this project meets it |
|---|---|
| Console-based program | Uses numbered text menus in `main.py` |
| Event records | Create, view, search, update and cancel events |
| Event information | Stores name, date, time, venue, capacity and status |
| Venue records | Add and view venues, including their capacity |
| Attendee records | Register attendees and save name, phone and email |
| Event registration | Connects an attendee to an event |
| Unique registration ID | Generates IDs such as `REG006` |
| Optional fee tracking | Stores a fee and Paid/Unpaid status |
| Reports | Shows attendees for an event and remaining places |
| Unique IDs | Generates IDs for events, venues, attendees and registrations |
| Valid date | Checks date format `YYYY-MM-DD` |
| Positive capacity | Rejects zero or negative capacity |
| Event capacity | Prevents registrations after the event is full |
| Events by date | Event lists and reports are sorted by date |
| CSV storage | Uses four CSV files in the `data` folder |
| CSV headings | Creates each CSV file and its headings when missing |
| Python functions | Features are separated into functions and modules |
| Error handling | Uses `try/except` for invalid dates, numbers and fees |
| Minimum 30 records | The supplied sample data contains 30 records total |
| No GUI / SQL / API | The program is a basic console application and uses CSV only |

### What the project does not include

The assignment says recurring events and automatic venue-conflict detection are not required. This project does not add those features. It also does not include a graphical interface, SQL database, API, online payment gateway or automated email.

## 3. Sample data included

The sample data is deliberately small: **30 records total**, not 30 in every file.

| CSV file | Sample records |
|---|---:|
| `venues.csv` | 10 |
| `events.csv` | 10 |
| `attendees.csv` | 5 |
| `registrations.csv` | 5 |
| **Total** | **30** |

The sample event names and venues are based on real Liberia event listings and public observances. Examples include the National County Sports Meet, Monrovia Fest, LINFFEST, Orange 5G Fest, Liberia Book Festival, National Flag Day and the Samuel Kanyon Doe Sports Complex.

**Accuracy note:** Some event listings may change. The 2026 event names, dates and venues were taken from public listings available during project preparation. Sample times, attendee names, contact details and venue/event capacities are demonstration data, not official organizer information. Confirm current details with event organizers before using the program for a real event.

Sources:
- Ministry of Youth & Sports, National County Sports Meet opening update: https://www.moys.gov.lr/media/press-releases/ministry-youth-sports-announces-change-hosting-arrangements-2026-national
- Liberia events listing: https://unforgettableliberia.com/?page=events
- Ministry of Education, 179th National Flag Day: https://flagday.moe.gov.lr/flag-day

## 4. How to run the program

1. Extract the ZIP file.
2. Open the `Event_Management_System_Final` folder in Visual Studio Code.
3. Open **Terminal > New Terminal**.
4. Enter:

```powershell
py main.py
```

If `py` does not work, use the full path to your installed Python executable, for example:

```powershell
& "C:\Users\AdminUser\AppData\Local\Programs\Python\Python314\python.exe" main.py
```

No extra Python packages are needed.

## 5. Main menu

1. Event Management
2. Venue Management
3. Attendee Management
4. Registration Management
5. Reports
6. View All Events
0. Exit

Choose a number and press Enter. Each section has its own menu. Choose `0` to return to the previous menu.

## 6. CSV files

The `data` folder contains:
- `events.csv`
- `venues.csv`
- `attendees.csv`
- `registrations.csv`

The program reads and writes the records in these files. Do not change the column headings.

## 7. Important rules in the program

- An event must use an existing venue.
- Event capacity must be greater than zero and cannot exceed the venue capacity.
- An event's capacity cannot be reduced below its current active registrations.
- A registration must use an existing attendee and event.
- The same attendee cannot have two active registrations for the same event.
- A full event cannot accept another registration.
- A cancelled event cannot accept registrations.
- Cancelling an event also cancels its active registrations.
- Cancelled registrations do not count toward the remaining places.

## 8. Suggested demonstration for the class

1. Start the program and show the main menu.
2. View the existing events and venues.
3. Add one attendee.
4. Create a test event.
5. Register the attendee for the test event.
6. View the attendee list and remaining places.
7. Update the registration payment to Paid.
8. Show the reports.
9. Explain that the records are saved in CSV files.

## 9. Project folder

- `main.py` – main menu and program start
- `storage.py` – creates, reads and writes CSV files
- `helpers.py` – input validation, ID generation and table display
- `events.py` – event management
- `venues.py` – venue management
- `attendees.py` – attendee management
- `registrations.py` – event registration and payment status
- `reports.py` – attendance and payment reports
- `data/` – CSV records
- `presentation/` – five-person presentation guide
- `tests/` – simple tests for CSV storage
