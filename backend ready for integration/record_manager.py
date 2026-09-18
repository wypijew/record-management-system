# record_manager.py
# creating, finding, getting, creating, deleting, updating record

from validators import record_id_for, record_type_for, validate_record


def id_exists(records, record_id):
    """
    Check whether a record with the specified ID exists.

    @param records: List of records to search.
    @param record_id: ID of the record to find.
    @return: True if the record ID exists; otherwise False.
    """
    for record in records:
        if record_id_for(record) == record_id:
            return True
    return False


def find_record_by_id(records, record_id, record_type=None):
    """
    Find and return a record with the specified ID.

    @param records: List of records to search.
    @param record_id: ID of the record to find.
    @return: Matching record if found; otherwise None.
    """
    for record in records:
        type_matches = (
            record_type is None
            or record_type_for(record) == record_type
        )
        if record_id_for(record) == record_id and type_matches:
            return record
    return None


def get_records_by_type(records, record_type):
    """
    Return all records matching the specified record type.

    @param records: List of records to search.
    @param record_type: Type of records to return.
    @return: List of records matching the specified type.
    """
    return [
        record for record in records
        if record_type_for(record) == record_type
    ]


def search_records(records, record_id=None, record_type=None):
    """
    Search records using the specified ID and record type.

    @param records: List of records to search.
    @param record_id: Optional ID used to filter records.
    @param record_type: Optional record type used to filter records.
    @return: List of records matching the specified criteria.
    """
    results = []

    for record in records:
        if record_id is not None and record_id_for(record) != record_id:
            continue
        if record_type is not None and record_type_for(record) != record_type:
            continue
        results.append(record)

    return results


def create_record(records, new_record):
    """
    Validate and add a new record to the records list.

    @param records: List of existing records.
    @param new_record: New record to validate and add.
    @return: True if the record is added; otherwise False.
    """
    if not validate_record(new_record, records):
        return False

    records.append(new_record)
    return True


def delete_record(records, record_id, record_type=None):
    """
    Delete a record with the specified ID and optional record type.

    @param records: List of records to search.
    @param record_id: ID of the record to delete.
    @param record_type: Optional record type used to identify the record.
    @return: True if the record is deleted; otherwise False.
    """
    for record in records:
        if record_id_for(record) == record_id:
            if record_type is None or record_type_for(record) == record_type:
                records.remove(record)
                return True
    return False


def update_record(records, record_id, updated_data, record_type=None):
    """
    Update a record with the specified ID and optional record type.

    @param records: List of records to search.
    @param record_id: ID of the record to update.
    @param updated_data: Dictionary containing the fields to update.
    @param record_type: Optional record type used to identify the record.
    @return: True if the record is updated; otherwise False.
    """
    for record in records:
        if record_id_for(record) == record_id:
            if (
                record_type is not None
                and record_type_for(record) != record_type
            ):
                continue

            updated_record = record.copy()
            updated_record.update(updated_data)

            if not validate_record(
                updated_record, records, current_id=record_id
            ):
                return False

            record.update(updated_data)
            return True

    return False
