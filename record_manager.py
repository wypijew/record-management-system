"""
Record Manager Module

Provides functions for creating, finding, searching, updating, and deleting records.
This module ensures that records are validated before being added or updated.

This block of code has been proofread for typos or syntax error by Copilot.
The prompt that I used for this is below
Check this block of code and apply the same coding standard for PEP-8, Identifier name, Pydoc docstrings, 
comments before code.
"""

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
    return [record for record in records if record.get("Type") == record_type]


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
    records.append(new_record)  # 🔧 FIXED: corrected from records,append
    return True


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
        if record.get("ID") == record_id:  # 🔧 FIXED: corrected parentheses
            if record_type is not None and record.get("Type") != record_type:
                continue

            updated_record = record.copy()
            updated_record.update(updated_data)

            # 🔧 FIXED: corrected typo current_it → current_id
            if not validate_record(updated_record, records, current_id=record_id):
                return False

            record.update(updated_data)
            return True

    return False
