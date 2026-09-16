"""
Main backend entry point for record management system.

This script connects the different modules (models, record manager, storage)
and demonstrates how records can be created, updated, searched, and deleted.
It can be used for initial testing before the GUI is built.
"""
# REVIEW: I removed the Copilot-related section from the module docstring,
# as this is not an appropriate place for this information. Please remove
# this REVIEW comment as well after reading it.


from models import make_client_record, make_airline_record, make_flight_record
# REVIEW: Please split the long import statements across multiple lines
# to keep them within the recommended 79-character line limit.
# as below
from record_manager import (create_record, search_records, update_record,
                            delete_record)
from storage import load_records, save_records

# Constants should be uppercase with underscores
FILENAME = "records.json"


def main() -> None:
    """
    Main function to demonstrate backend functionality.

    Loads records from storage, creates sample records, performs CRUD
    operations, and saves the updated records back to storage.
    """
    # Load existing records from file
    records = load_records(FILENAME)

    # REVIEW: This point remains from the previous review. These fixed sample
    # records are useful for testing the backend, but should be removed before
    # final GUI integration. Otherwise, the application will attempt to create
    # the same test records each time it starts.
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
        # REVIEW: The keyword arguments used here must match the parameter names
        # in make_flight_record(). Please update them after the Flight record
        # terminology in models.py has been corrected, so that both modules use
        # the same Start City and End City naming consistently.
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


# REVIEW SUMMARY:
# The latest revision addresses several issues identified in the previous
# review. The overall formatting has been significantly improved, and a
# module docstring, function docstring, type hint, consistent indentation,
# and descriptive comments have been added.
#
# Several functional issues have also been corrected. The missing comma in
# the Client sample data has been added, the Flight record is now created
# before it is passed to create_record(), and the syntax error in the
# update_record() call has been fixed.
#
# Thank you for addressing these points and for the improvements made to
# this version.
#
# Remaining REVIEW comments can be found at:
# - Lines 8-10: removal of the Copilot-related information.
# - Lines 14-16: formatting of long import statements.
# - Lines 35-38: removal of fixed sample records before GUI integration.
# - Lines 63-66: consistency of Flight keyword argument names.
#
# Please check all REVIEW comments before the final version is integrated.