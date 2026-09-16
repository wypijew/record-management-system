from datetime import datetime

# REVIEW: Remove the Copilot proofreading note and prompt from the final
# code. The indented standalone string at module level may also cause an
# IndentationError. If a module docstring is required, place it before the
# import statement and keep it focused on the purpose of this module.
    """
    This py file has been corrected from the initial version of the code by CoPilot with the prompt,
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
    # REVIEW: This issue remains from the previous review. Use
    # type(record_id) is int instead of isinstance(record_id, int) so that
    # boolean values are rejected, as isinstance(True, int) returns True.
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

    # REVIEW: Address Line 2 and Address Line 3 are part of the Client record
    # structure specified in the assignment brief, so their presence should
    # also be validated. However, the brief does not require these optional
    # address lines to contain non-empty values. If they are added to
    # required_fields, please also adjust the validation below so that
    # Address Line 2 and Address Line 3 can be empty strings.
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
    # REVIEW: This issue remains from the previous review. Replace
    # "Airline Name" with "Company Name" throughout this function to match
    # the Airline record structure specified in the assignment brief.
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
    # REVIEW: This issue remains from the previous review. Replace
    # "Departure" and "Arrival" with "Start City" and "End City" throughout
    # this function to match the Flight record structure specified in the
    # assignment brief.
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

    # REVIEW: This issue remains from the previous review. Please use
    # validate_id() for both Client_ID and Airline_ID instead of separate
    # isinstance() checks. Once validate_id() is corrected as noted above,
    # this will consistently reject zero, negative IDs, and boolean values.
    # Remember that isinstance(True, int) returns True in Python
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

    # REVIEW: This issue remains from the previous review. Please validate
    # record["ID"] before checking its uniqueness, for example:
    # if not validate_id(record["ID"]):
    #     return False
    # validate_id() checks whether the ID itself is valid, while
    # validate_unique_id() only checks whether that ID already exists.
    if not validate_unique_id(records, record["ID"], current_id=current_id):
        return False

    if record["Type"] == "Client":
        return validate_client_record(record)

    if record["Type"] == "Airline":
        return validate_airline_record(record)

    if record["Type"] == "Flight":
        return validate_flight_record(record, records)

    return False


# REVIEW SUMMARY:
# The latest revision addresses several issues identified in the previous
# review. The indentation and general formatting have been significantly
# improved, and type hints and docstrings have been added throughout the
# module.
#
# Several functional issues have also been corrected. In particular,
# client_exists() and airline_exists() now check all records before
# returning False, and the previous syntax, spelling, and indentation
# errors in these functions have been resolved. The date validation has
# also been corrected to use a valid hour and minute format, and several
# other previously identified typos and validation issues have been fixed.
#
# Thank you for addressing these points and for the improvements made to
# this version.
#
# Remaining REVIEW comments can be found at:
# - Lines 3-6: module documentation and the Copilot proofreading note.
# - Lines 36-38: ID validation and boolean values.
# - Lines 109-114: Client record structure and optional address fields.
# - Lines 161-163: Airline record terminology.
# - Lines 190-193: Flight record terminology.
# - Lines 208-212: Client_ID and Airline_ID validation.
# - Lines 255-260: ID validation before the uniqueness check.
#
# Please check all REVIEW comments before the final version is integrated.