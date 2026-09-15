from datetime import datetime
    """
    This py file has been corrected by CoPilot with the prompt,
    This is the block of code that I have written.
    Now check for any typos or indentation errors that could cause syntax citation.
    The standard for you to use when proofreading my code is provided below:
    enter University guideline
    """
    
# Constants should be uppercase with underscores
VALID_TYPES = {"Client", "Airline", "Flight"}


def validate_record_type(record_type: str) -> bool:
    """
    Checks if the given record type is valid.

    @param record_type: String representing the type of record
    @return: True if the record type is one of VALID_TYPES, False otherwise
    """
    return record_type in VALID_TYPES


def validate_id(record_id: int) -> bool:
    """
    Validates that a record ID is a positive integer.

    @param record_id: Integer ID to validate
    @return: True if the ID is a positive integer, False otherwise
    """
    return isinstance(record_id, int) and record_id > 0


def validate_unique_id(records: list, record_id: int, current_id: int = None) -> bool:
    """
    Ensures that the record ID is unique among existing records.

    @param records: List of dictionaries containing existing records
    @param record_id: ID to validate
    @param current_id: Optional current ID (used when updating an existing record)
    @return: True if the ID is unique, False otherwise
    """
    for record in records:
        if record.get("ID") == record_id:
            if current_id is not None and record_id == current_id:
                continue
            return False
    return True


def validate_date(date_string: str) -> bool:
    """
    Validates that the date string matches the format YY-MM-DD HH:MM.

    @param date_string: String representing the date
    @return: True if the date is valid, False otherwise
    """
    try:
        datetime.strptime(date_string, "%y-%m-%d %H:%M")
        return True
    except ValueError:
        return False


def client_exists(records: list, client_id: int) -> bool:
    """
    Checks if a client record exists in the records list.

    @param records: List of dictionaries containing existing records
    @param client_id: ID of the client to check
    @return: True if the client exists, False otherwise
    """
    for record in records:
        if record.get("Type") == "Client" and record.get("ID") == client_id:
            return True
    return False


def airline_exists(records: list, airline_id: int) -> bool:
    """
    Checks if an airline record exists in the records list.

    @param records: List of dictionaries containing existing records
    @param airline_id: ID of the airline to check
    @return: True if the airline exists, False otherwise
    """
    for record in records:
        if record.get("Type") == "Airline" and record.get("ID") == airline_id:
            return True
    return False


def validate_client_record(record: dict) -> bool:
    """
    Validates that a client record contains all required fields and valid data.

    @param record: Dictionary containing client record data
    @return: True if the client record is valid, False otherwise
    """
    required_fields = [
        "ID", "Type", "Name", "Address Line 1", "City",
        "State", "Zip Code", "Country", "Phone Number"
    ]

    for field in required_fields:
        if field not in record:
            return False

    if not validate_id(record["ID"]):
        return False

    if record["Type"] != "Client":
        return False

    if not str(record["Name"]).strip():
        return False

    if not str(record["Address Line 1"]).strip():
        return False

    if not str(record["City"]).strip():
        return False

    if not str(record["State"]).strip():
        return False

    if not str(record["Zip Code"]).strip():
        return False

    if not str(record["Country"]).strip():
        return False

    if not str(record["Phone Number"]).strip():
        return False

    return True


def validate_airline_record(record: dict) -> bool:
    """
    Validates that an airline record contains all required fields and valid data.

    @param record: Dictionary containing airline record data
    @return: True if the airline record is valid, False otherwise
    """
    required_fields = ["ID", "Type", "Airline Name"]

    for field in required_fields:
        if field not in record:
            return False

    if not validate_id(record["ID"]):
        return False

    if record["Type"] != "Airline":
        return False

    if not str(record["Airline Name"]).strip():
        return False

    return True


def validate_flight_record(record: dict, records: list) -> bool:
    """
    Validates that a flight record contains all required fields and valid references.

    @param record: Dictionary containing flight record data
    @param records: List of existing records to check client and airline references
    @return: True if the flight record is valid, False otherwise
    """
    required_fields = [
        "ID", "Type", "Client_ID", "Airline_ID", "Date", "Departure", "Arrival"
    ]

    for field in required_fields:
        if field not in record:
            return False

    if not validate_id(record["ID"]):
        return False

    if record["Type"] != "Flight":
        return False

    if not isinstance(record["Client_ID"], int):
        return False

    if not isinstance(record["Airline_ID"], int):
        return False

    if not client_exists(records, record["Client_ID"]):
        return False

    if not airline_exists(records, record["Airline_ID"]):
        return False

    if not validate_date(record["Date"]):
        return False

    if not str(record["Departure"]).strip():
        return False

    if not str(record["Arrival"]).strip():
        return False

    return True


def validate_record(record: dict, records: list, current_id: int = None) -> bool:
    """
    Validates a record based on its type and uniqueness.

    @param record: Dictionary containing record data
    @param records: List of existing records
    @param current_id: Optional current ID (used when updating an existing record)
    @return: True if the record is valid, False otherwise
    """
    if "Type" not in record:
        return False

    if not validate_record_type(record["Type"]):
        return False

    if "ID" not in record:
        return False

    if not validate_unique_id(records, record["ID"], current_id=current_id):
        return False

    if record["Type"] == "Client":
        return validate_client_record(record)

    if record["Type"] == "Airline":
        return validate_airline_record(record)

    if record["Type"] == "Flight":
        return validate_flight_record(record, records)

    return False

  
