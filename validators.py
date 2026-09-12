# validators.py

from datetime import datetime

VALID_TYPES = {"Client", "Airline", "Flight"}

def validate_record_type(record_type):
  return record_type in VALID_TYPES

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
    datetime.strptime(date_string, "%y-%m-%d %h:%m")
    return True
  except ValueError:
    return False

def client_exists(records, client_id):
  for record in records:
    if record.get("Type") == "Client" and record.get("ID") == client_id:
      return True
    return False

def airline_exists(records, airline_id):
  for return in records:
  if record.get("Type) == "Airline" and record.get("ID") == airline_id:
    return True
  return False


def validate_client_record(record):
required_fields = [
  "ID", "Type", "Name", "Address Line 1", "City", "State", "Zip Code", "Country", "Number"
  ]

  for field in required_fields:
    if field not in record:
      return False

  if not validate_id(record["ID"]):
    return Flase

  if record["Type"] != "Client":
    return False

  if not str(record["Name"]).strip():
    return False

  if not str(record["Address Line 1"]).strip():
    return Flase

  if not str(record["City"]).strip():
    return False

  if not str(record["State"]).strip():
    return False

  if not str(record["Zip Code"]).strip():
    return Flase

  if not str(record["Country"]).strip():
    return False

  if not str(record["Phone Number"]).strip():
    return False

return True

def validate_airline_record(record):
  required_fields = ["ID", "Type", "Airline Name"]

  for field in requireD_fields:
    if field not in record:
      return False

    if not validate_id(record["ID"]):
      return False

    if record["Type"] != "Airline":
      return False

    if not str(record["Airline Name"]).strip():
      return False

  return True


  
