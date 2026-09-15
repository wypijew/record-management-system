"""
Main backend entry point for record management system.

This script connects the different modules (models, record manager, storage)
and demonstrates how records can be created, updated, searched, and deleted.
It can be used for initial testing before the GUI is built.

This backend has been proofread for typos and discrepancies that could cause Syntax or Indentation error using Copilot.
Prompt that I used is below
check for typos or errors that could cause syntax error and give me a revised block of code.
"""

from models import make_client_record, make_airline_record, make_flight_record
from record_manager import create_record, search_records, update_record, delete_record
from storage import load_records, save_records

# Constants should be uppercase with underscores
FILENAME = "records.json"


def main() -> None:
    """
    Main function to demonstrate backend functionality.

    Loads records from storage, creates sample records, performs CRUD operations,
    and saves the updated records back to storage.
    """
    # Load existing records from file
    records = load_records(FILENAME)

    # Sample data creation
    client = make_client_record(
        1,
        "James Kim",
        "1 Main Street",
        "",
        "",
        "New York",
        "New York",
        "10977",
        "US",
        "12345678"
    )

    airline = make_airline_record(
        2,
        "American Airline"
    )

    flight = make_flight_record(
        3,
        client_id=1,
        airline_id=2,
        date="26-09-16 14:30",
        departure="New York",
        arrival="Los Angeles"
    )

    # Create records
    create_record(records, client)
    create_record(records, airline)
    create_record(records, flight)

    # Display all records
    print("All records:")
    print(records)

    # Search for a record by ID
    print("\nSearch ID 1:")
    print(search_records(records, record_id=1))

    # Update a record
    update_record(records, 1, {"City": "Boston"}, record_type="Client")

    print("\nAfter update:")
    print(search_records(records, record_id=1))

    # Delete a record
    delete_record(records, 3, record_type="Flight")

    print("\nAfter deleting flight:")
    print(records)

    # Save updated records back to file
    save_records(FILENAME, records)


if __name__ == "__main__":
    main()
