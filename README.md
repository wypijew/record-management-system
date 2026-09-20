# Record Management System

## Project purpose

This project is a Python record management application for a specialist travel agent. It uses a Tkinter graphical user interface to create, search, display, update and delete Client, Airline and Flight records.

Records are held in one shared list of dictionaries and retained between application sessions using JSON storage.

## Features

The application supports the following operations for each required record type:

- create a record;
- search for and display a record;
- update a record;
- delete a record;
- validate data before records are created or updated;
- load stored records when the application starts; and
- save records when the application closes.

## Record structure

### Client

Client records contain:

- `ID`
- `Type`
- `Name`
- `Address Line 1`
- `Address Line 2`
- `Address Line 3`
- `City`
- `State`
- `Zip Code`
- `Country`
- `Phone Number`

`Address Line 2` and `Address Line 3` must be present but may be empty.

### Airline

Airline records contain:

- `ID`
- `Type`
- `Company Name`

### Flight

Flight records contain:

- `Flight_ID`
- `Client_ID`
- `Airline_ID`
- `Date`
- `Start City`
- `End City`

## Data and integration contract

The GUI and backend use one shared list of record dictionaries.

Client and Airline records use `ID` as their identifier and include a `Type` field with the value `Client` or `Airline`. Flight records use `Flight_ID`. The GUI does not need to provide a `Type` field for a Flight record.

The GUI must use the exact Flight field names shown above. The backend validates records before create and update operations and checks that the Client and Airline IDs referenced by a Flight record exist.

## Validation

The application validates:

- supported record types;
- positive integer record IDs;
- unique IDs within a record type;
- required and optional text fields;
- referenced Client and Airline records for Flights; and
- date and time input.

Flight dates must use the following format:

`YY-MM-DD HH:MM`

## Persistent storage

Records are stored in JSON format in:

`src/data/records.json`

When the application starts, it loads stored records into the shared list.
When it closes normally, it saves the current shared list to the same file.

## Requirements

- Python 3
- dependencies listed in `requirements.txt`

Install the project dependencies from the repository root:

```console
pip install -r requirements.txt
```

## Running the application

From the project root, run:

```console
python main.py
```

Close the application through the **Exit** button or the window close button so that records are saved.

## Testing

Run the automated unit tests from the project root:

```console
python -m pytest -q
```

The final automated suite contains 250 passing unit tests. It covers the validators, models, record management, storage and application entry point. Coverage.py confirmed 100% coverage of the implemented backend modules.

Manual end-to-end testing of the integrated application also passed all 23 test cases. These tests cover record operations, validation messages, data persistence and failed operations that must not change stored data.

The completed manual test form is available in:

`tests/manual_tests/Manual End-to-End Test Cases.docx`

A PDF copy of the completed manual end-to-end test form is available in:

`docs/Completed Manual End-to-End Test Cases.pdf`

## Project structure

```text
main.py                                         Application launcher
requirements.txt                                Project dependencies
README.md                                       Project documentation
docs/Completed Manual End-to-End Test Cases.pdf Completed manual test evidence
src/main.py                                     Application entry point
src/conf/                                       Configuration directory
src/data/storage.py                             JSON loading and saving
src/data/records.json                           Persistent application data
src/gui/app.py                                  Tkinter graphical user interface
src/record/models.py                            Record structure creation
src/record/record_manager.py                    Create, search, update and delete operations
src/record/validators.py                        Record and field validation
tests/unit_tests/                               Automated unit tests
tests/manual_tests/                             Completed manual end-to-end test form
```

## Repository

GitHub repository: [record-management-system](https://github.com/wypijew/record-management-system)