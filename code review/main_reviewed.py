"""
REVIEW: Please apply the University's "Coding Standard" consistently
throughout this file. Use 4 spaces per indentation level and keep code
lines within the recommended 79-character limit.

Please also use two blank lines between top-level function definitions.

Add appropriate comments/documentation before each self-contained block
of code to explain its purpose and intended logic.

Please also add docstrings to functions in accordance with the
University's Coding Standard. Docstrings should describe the function's
purpose, input parameters and return values.

Please refer to the "Coding Standard" document for the full formatting
and documentation guidance.
"""

# this is how the backend pieces will connect
# can use for initial testing before GUI is built


#main.py

from models import make_client_record, make_airline_record, make_flight_record
from record_manager import create_record, search_records, update_record, delete_record
from storage import load_records, save_records

FILENAME = "records.json"


def main():
  records = load_records(FILENAME)

  # REVIEW: This sample-data block is useful for initial backend testing,
  # but consider removing or separating it before final GUI integration.
  # Since existing records are loaded from persistent storage at startup,
  # repeatedly creating fixed sample IDs may conflict with stored records.

  # REVIEW: Add a comma between "US" and "12345678".
  # Without the comma, Python concatenates the adjacent string literals
  # into "US12345678", so make_client_record() receives too few arguments.
  # Sample data creation

  client = make_client_record(
    1, "James Kim", "1 Main Street", "", "", "Newyork", "Newyork", "10977", "US" "12345678"
  )

  airline = make_airline_record(2, "American Airline"
                               )

  create_record(records, client)
  create_record(records, airline)
  # REVIEW: Create a Flight record before attempting to add it to records.
  # The variable "flight" has not been defined, so this statement would
  # raise a NameError when executed.
  create_record(records, flight)

  print("All records:")
  print(records)

  print("\nSearch ID 1:")
  print(search_records(records, record_id=1))

  # REVIEW: Replace the dot after {"City": "Boston"} with a comma.
  # Function arguments must be separated by commas. The current statement
  # contains invalid syntax and prevents main.py from being executed.
  update_record(records, 1, {"City": "Boston"}. record_type="Client")

  print("\nAfter update:")
  print(search_records(records, record_id=1))

  delete_record(records, 3, record_type="Flight")

  print("\nAfter deleting flight:")
  print(records)

  save_records(FILENAME, records)

if __name__ == "__main__":
  main()
