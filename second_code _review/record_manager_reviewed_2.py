"""
Record Manager Module

Provides functions for creating, finding, searching, updating, and deleting records.
This module ensures that records are validated before being added or updated.
"""
# REVIEW: I removed the Copilot-related section from the module docstring,
# as this is not an appropriate place for this information. Please remove
# this REVIEW comment as well after reading it.

from validators import validate_record


def id_exists(records: list, record_id: int) -> bool:
    """
    Checks if a record with the given ID exists.

    @param records: List of record dictionaries
    @param record_id: ID to check
    @return: True if the ID exists, False otherwise
    """
    for record in records:
        if record.get("ID") == record_id:
            return True
    return False


def find_record_by_id(records: list, record_id: int) -> dict | None:
    """
    Finds a record by its ID.

    @param records: List of record dictionaries
    @param record_id: ID to search for
    @return: The record dictionary if found, None otherwise
    """
    for record in records:
        if record.get("ID") == record_id:
            return record
    return None


def get_records_by_type(records: list, record_type: str) -> list:
    """
    Retrieves all records of a given type.

    @param records: List of record dictionaries
    @param record_type: Type of record to filter by
    @return: List of records matching the type
    """
    # REVIEW: The syntax issue from the previous review has been corrected.
    # Please also split the return statement across multiple lines to keep
    # the code within the 79-character line limit.
    return [record for record in records if record.get("Type") == record_type]

# REVIEW: The previous syntax issue with the default parameter has been
# corrected. Please also split this function definition across multiple
# lines to keep it within the recommended 79-character line limit.
def search_records(records: list, record_id: int = None, record_type: str = None) -> list:
    """
    Searches records by ID and/or type.

    @param records: List of record dictionaries
    @param record_id: Optional ID to filter by
    @param record_type: Optional type to filter by
    @return: List of matching records
    """
    results = []

    for record in records:
        if record_id is not None and record.get("ID") != record_id:
            continue
        if record_type is not None and record.get("Type") != record_type:
            continue
        results.append(record)

    return results


def create_record(records: list, new_record: dict) -> bool:
    """
    Creates a new record if it is valid.

    @param records: List of existing records
    @param new_record: Dictionary representing the new record
    @return: True if record was added, False otherwise
    """
    if not validate_record(new_record, records):
        return False
    records.append(new_record)
    return True

# REVIEW: Please split this function definition across multiple lines to
# keep it within the recommended 79-character line limit.
def delete_record(records: list, record_id: int, record_type: str = None) -> bool:
    """
    Deletes a record by ID and optional type.

    @param records: List of existing records
    @param record_id: ID of the record to delete
    @param record_type: Optional type to filter by
    @return: True if record was deleted, False otherwise
    """
    for record in records:
        if record.get("ID") == record_id:
            if record_type is None or record.get("Type") == record_type:
                records.remove(record)
                return True
    return False

# REVIEW: Please split this function definition and any remaining
# long statements across multiple lines to keep them within the
# recommended 79-character line limit.
def update_record(records: list, record_id: int, updated_data: dict, record_type: str = None) -> bool:
    """
    Updates a record with new data if valid.

    @param records: List of existing records
    @param record_id: ID of the record to update
    @param updated_data: Dictionary of fields to update
    @param record_type: Optional type to filter by
    @return: True if record was updated, False otherwise
    """
    for record in records:
        if record.get("ID") == record_id:
            if record_type is not None and record.get("Type") != record_type:
                continue

            updated_record = record.copy()
            updated_record.update(updated_data)
            if not validate_record(updated_record, records, current_id=record_id):
                return False

            record.update(updated_data)
            return True

    return False


# REVIEW SUMMARY:
# The latest revision addresses the functional issues identified in the
# previous review. In particular, the syntax error in
# get_records_by_type() has been corrected, the default parameter in
# search_records() now uses the correct syntax, and create_record() now
# correctly uses the append() method.
#
# The issues previously identified in update_record() have also been
# corrected. The record.get() call is now syntactically correct,
# current_id is passed correctly to validate_record(), and the final
# return False statement has been moved outside the loop so that all
# records can be checked.
#
# Type hints, docstrings, consistent indentation, and spacing between
# top-level functions have also been added throughout the module.
#
# Thank you for addressing these points and for the improvements made to
# this version.
#
# Remaining REVIEW comments can be found at:
# - Lines 7-9: removal of the Copilot-related information.
# - Lines 50-52: formatting of get_records_by_type().
# - Lines 55-57: formatting of search_records().
# - Lines 92-93: formatting of delete_record().
# - Lines 110-112: formatting of update_record().
#
# Please check all REVIEW comments before the final version is integrated.