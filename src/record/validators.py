# validators.py

from datetime import datetime
from re import fullmatch


VALID_TYPES = {"Client", "Airline", "Flight"}


def validate_record_type(record_type):
    """
    Validate that the record type is supported.

    @param record_type: Record type to validate.
    @return: True if the record type is valid; otherwise False.
    """
    return isinstance(record_type, str) and record_type in VALID_TYPES


# 'type(record_id) is int' is used to reject boolean values,
# as isinstance(True, int) returns True in Python.
def validate_id(record_id):
    """
    Validate that a record ID is a positive integer.

    @param record_id: Record ID to validate.
    @return: True if the record ID is valid; otherwise False.
    """
    return type(record_id) is int and record_id > 0


def validate_required_text(value):
    """
    Validate that a required text field is a non-empty string.

    @param value: Value to validate.
    @return: True if the value is a non-empty string; otherwise False.
    """
    return isinstance(value, str) and bool(value.strip())


def validate_optional_text(value):
    """
    Validate that an optional text field is a string.

    @param value: Value to validate.
    @return: True if the value is a string; otherwise False.
    """
    return isinstance(value, str)


def record_id_for(record):
    """
    Return the ID field used by this record type.

    @param record: Record dictionary to inspect.
    @return: Flight_ID or ID, or None if unavailable.
    """
    if not isinstance(record, dict):
        return None

    if record_type_for(record) == "Flight":
        return record.get("Flight_ID")
    return record.get("ID")


def record_type_for(record):
    """
    Return the record type, including GUI-style Flight records.

    @param record: Record dictionary to inspect.
    @return: Record type string, or None if it cannot be identified.
    """
    if not isinstance(record, dict):
        return None

    # Infer Flight only when the Type key is absent, not invalid.
    if "Type" not in record and "Flight_ID" in record:
        return "Flight"

    record_type = record.get("Type")
    return record_type if validate_record_type(record_type) else None


def validate_unique_id(records, record_id, current_id=None, record_type=None):
    """
    Check ID uniqueness, optionally restricted to one record type.

    @param records: List of existing records.
    @param record_id: Record ID to check for uniqueness.
    @param current_id: Optional ID of the record being updated.
    @param record_type: Optional type for checking ID uniqueness.
    @return: True if the record ID is unique; otherwise False.
    """
    for record in records:
        if record_type is not None and record_type_for(record) != record_type:
            continue
        if record_id_for(record) == record_id:
            if current_id is not None and record_id == current_id:
                continue
            return False
    return True


def validate_date(date_string):
    """
    Validate a real date and time in strict YY-MM-DD HH:MM format.

    @param date_string: Date and time string to validate.
    @return: True if the date and time are valid; otherwise False.
    """
    if not isinstance(date_string, str):
        return False

    # Require two digits per component and exactly one separating space.
    pattern = r"[0-9]{2}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}"
    if fullmatch(pattern, date_string) is None:
        return False

    try:
        # Check calendar validity after checking the text format.
        datetime.strptime(date_string, "%y-%m-%d %H:%M")
        return True
    except (ValueError, TypeError):
        return False


def client_exists(records, client_id):
    """
    Check whether a Client with the specified ID exists.

    @param records: List of records to search.
    @param client_id: ID of the Client to find.
    @return: True if the Client exists; otherwise False.
    """
    for record in records:
        if (
            record.get("Type") == "Client"
            and record.get("ID") == client_id
        ):
            return True

    return False


def airline_exists(records, airline_id):
    """
    Check whether an Airline with the specified ID exists.

    @param records: List of records to search.
    @param airline_id: ID of the Airline to find.
    @return: True if the Airline exists; otherwise False.
    """
    for record in records:
        if (
            record.get("Type") == "Airline"
            and record.get("ID") == airline_id
        ):
            return True

    return False


def validate_client_record(record):
    """
    Validate the required fields and values of a Client record.

    @param record: Client record to validate.
    @return: True if the Client record is valid; otherwise False.
    """
    if not isinstance(record, dict):
        return False

    required_fields = [
        "ID",
        "Type",
        "Name",
        "Address Line 1",
        "Address Line 2",
        "Address Line 3",
        "City",
        "State",
        "Zip Code",
        "Country",
        "Phone Number"
    ]

    for field in required_fields:
        if field not in record:
            return False

    if not validate_id(record["ID"]):
        return False

    if record["Type"] != "Client":
        return False

    if not validate_required_text(record["Name"]):
        return False

    if not validate_required_text(record["Address Line 1"]):
        return False

    if not validate_optional_text(record["Address Line 2"]):
        return False

    if not validate_optional_text(record["Address Line 3"]):
        return False

    if not validate_required_text(record["City"]):
        return False

    if not validate_required_text(record["State"]):
        return False

    if not validate_required_text(record["Zip Code"]):
        return False

    if not validate_required_text(record["Country"]):
        return False

    if not validate_required_text(record["Phone Number"]):
        return False

    return True


def validate_airline_record(record):
    """
    Validate the required fields and values of an Airline record.

    @param record: Airline record to validate.
    @return: True if the Airline record is valid; otherwise False.
    """
    if not isinstance(record, dict):
        return False

    required_fields = ["ID", "Type", "Company Name"]

    for field in required_fields:
        if field not in record:
            return False

    if not validate_id(record["ID"]):
        return False

    if record["Type"] != "Airline":
        return False

    if not validate_required_text(record["Company Name"]):
        return False

    return True


def validate_flight_record(record, records):
    """
    Validate the required fields and values of a Flight record.

    @param record: Flight record to validate.
    @param records: List used to verify referenced records.
    @return: True if the Flight record is valid; otherwise False.
    """
    if not isinstance(record, dict):
        return False

    required_fields = [
        "Flight_ID", "Client_ID", "Airline_ID", "Date",
        "Start City", "End City"
    ]

    for field in required_fields:
        if field not in record:
            return False

    if not validate_id(record["Flight_ID"]):
        return False

    if record_type_for(record) != "Flight":
        return False

    # Validate both reference IDs as positive integers before checking
    # whether the corresponding Client and Airline records exist.
    # Using validate_id() instead of isinstance(..., int) also rejects
    # zero and negative integers, keeping ID validation consistent.
    if not validate_id(record["Client_ID"]):
        return False

    if not validate_id(record["Airline_ID"]):
        return False

    if not client_exists(records, record["Client_ID"]):
        return False

    if not airline_exists(records, record["Airline_ID"]):
        return False

    if not validate_date(record["Date"]):
        return False

    if not validate_required_text(record["Start City"]):
        return False

    if not validate_required_text(record["End City"]):
        return False

    return True


def validate_record(record, records, current_id=None):
    """
    Validate a record according to its record type.

    @param record: Record to validate.
    @param records: List of existing records.
    @param current_id: Optional ID of the record being updated.
    @return: True if the record is valid; otherwise False.
    """
    if not isinstance(record, dict):
        return False

    record_type = record_type_for(record)
    if not validate_record_type(record_type):
        return False

    id_field = "Flight_ID" if record_type == "Flight" else "ID"
    if id_field not in record:
        return False

    # Validate the ID before checking uniqueness to maintain a clear
    # validation sequence: first check that the ID exists, then verify
    # that it is valid, and finally confirm that it is unique.
    if not validate_id(record[id_field]):
        return False

    if not validate_unique_id(
        records, record[id_field], current_id=current_id,
        record_type=record_type
    ):
        return False

    if record_type == "Client":
        return validate_client_record(record)

    if record_type == "Airline":
        return validate_airline_record(record)

    if record_type == "Flight":
        return validate_flight_record(record, records)

    return False
