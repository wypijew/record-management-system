# validators.py
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


from datetime import datetime

VALID_TYPES = {"Client", "Airline", "Flight"}

# REVIEW: Use 4 spaces per indentation level, as recommended by the
# University's Coding Standard.
def validate_record_type(record_type):
  return record_type in VALID_TYPES

# REVIEW: Use type(record_id) is int to reject boolean values,
# as isinstance(True, int) returns True in Python.
def validate_id(record_id):
  return isinstance(record_id, int) and record_id > 0

def validate_unique_id(records, record_id, current_id=None):
  for record in records:
    if record.get("ID") == record_id:
      if current_id is not None and record_id == current_id:
        continue
      return False
  return True

def validate_date(date_string):
  try:
    # REVIEW: The datetime format is incorrect. If the agreed format is
    # YYYY-MM-DD HH:MM, this should be "%Y-%m-%d %H:%M", for example,
    # 2026-09-14 14:00.
    datetime.strptime(date_string, "%y-%m-%d %h:%m")

    return True
  except ValueError:
    return False

def client_exists(records, client_id):
  for record in records:
    if record.get("Type") == "Client" and record.get("ID") == client_id:
      return True

    # REVIEW: return False is inside the loop, so only the first record
    # is checked. Move it outside the loop so all records are searched.
    return False



def airline_exists(records, airline_id):
  # REVIEW: Replace "return" with "record". "return" is a Python keyword
  # and cannot be used as a loop variable.
  for return in records:
  # REVIEW: This if statement must be indented inside the for loop.
  # Also add the missing closing quotation mark after "Type"; the
  # current syntax error prevents validators.py from being imported.
  if record.get("Type) == "Airline" and record.get("ID") == airline_id:
    return True

  # REVIEW: Move return False outside the loop so all records are
  # checked before the function concludes that the Airline does not exist.
  return False



def validate_client_record(record):
# REVIEW: Indent required_fields so it is inside validate_client_record().
# REVIEW: Add "Address Line 2" and "Address Line 3" to match the brief,
# and replace "Number" with "Phone Number". Use field names consistently
# throughout the code, as mismatched dictionary keys can cause valid
# records to be rejected and lead to errors or failing tests.
required_fields = [
  "ID", "Type", "Name", "Address Line 1", "City", "State", "Zip Code", "Country", "Number"
  ]

  for field in required_fields:
    if field not in record:
      return False

  if not validate_id(record["ID"]):
    # REVIEW: Typo: change "Flase" to "False". Otherwise Python treats
    # "Flase" as a name and raises a NameError when this branch executes.
    return Flase

  if record["Type"] != "Client":
    return False

  if not str(record["Name"]).strip():
    return False

  if not str(record["Address Line 1"]).strip():
    # REVIEW: Typo: change "Flase" to "False".
    return Flase

  if not str(record["City"]).strip():
    return False

  if not str(record["State"]).strip():
    return False

  if not str(record["Zip Code"]).strip():
    # REVIEW: Typo: change "Flase" to "False".
    return Flase

  if not str(record["Country"]).strip():
    return False

  if not str(record["Phone Number"]).strip():
    return False

# REVIEW: Indent this return so it remains inside validate_client_record().
return True

def validate_airline_record(record):
  required_fields = ["ID", "Type", "Airline Name"]
  # REVIEW: Replace "Airline Name" with "Company Name" to match the
  # assignment brief and use the same field name consistently across
  # models, validation, GUI and tests.

  for field in required_fields:
    if field not in record:
      return False

    # REVIEW: The validation checks below should be outside the for loop.
    # The loop should only check that all required fields are present;
    # otherwise the same validations are repeated for every field.
    if not validate_id(record["ID"]):
      return False

    if record["Type"] != "Airline":
      return False

    if not str(record["Airline Name"]).strip():
      return False

  return True

def validate_flight_record(record, records):
  required_fields = [
    "ID", "Type", "Client_ID", "Airline_ID", "Date", "Departure", "Arrival"
  ]
  # REVIEW: Replace "Departure" and "Arrival" with "Start City" and
  # "End City" to match the field names specified in the assignment
  # brief and keep them consistent across all modules.

  for field in required_fields:
    if field not in record:
      return False

  if not validate_id(record["ID"]):
    return False

  # REVIEW: Typo: change "Flgiht" to "Flight". As written, a valid
  # Flight record with Type "Flight" will always be rejected.
  if record["Type"] != "Flgiht":
    return False

  if not isinstance(record["Client_ID"], int):
    return False

  if not isinstance(record["Airline_ID"], int):
    return False

  """
  REVIEW: Use validate_id() for both reference IDs instead of
  isinstance(..., int). This validates them as positive integers before
  checking whether the corresponding Client and Airline records exist.
  It also rejects zero and negative integers, keeping ID validation
  consistent throughout the application.

  Suggested change:

  if not validate_id(record["Client_ID"]):
      return False

  if not validate_id(record["Airline_ID"]):
      return False
  """

  if not client_exists(records, record["Client_ID"]):
    return False

  if not airline_exists(records, record["Airline_ID"]):
    return False

  if not validate_date(record["Date"]):
    return False

  # REVIEW: Replace "Departure" and "Arrival" with "Start City" and
  # "End City" to match the assignment brief and keep the field names
  # consistent across the application.
  if not str(record["Departure"]).strip():
    return False

  if not str(record["Arrival"]).strip():
    return False

  return True

def validate_record(record, records, current_id=None):
  if "Type" not in record:
    return False

  if not validate_record_type(record["Type"]):
    return False

  if "ID" not in record:
    return False

  """
  REVIEW: Validate the ID before checking uniqueness to maintain a clear
  validation sequence: first check that the ID exists, then verify that
  it is valid, and finally confirm that it is unique.

  Suggested change:

  if not validate_id(record["ID"]):
      return False
  """
  if not validate_unique_id(records, record["ID"], current_id=current_id):
    return False

  if record["Type"] == "Client":
    return validate_client_record(record)

  if record["Type"] == "Airline":
    return validate_airline_record(record)

  if record["Type"] == "Flight":
    return validate_flight_record(record, records)

  return False



