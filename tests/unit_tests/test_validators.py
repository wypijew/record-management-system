"""Unit tests for validators.py using the GUI integration format."""

import pytest

import validators
from validators import (
    airline_exists,
    client_exists,
    record_id_for,
    record_type_for,
    validate_airline_record,
    validate_client_record,
    validate_date,
    validate_flight_record,
    validate_id,
    validate_optional_text,
    validate_record,
    validate_record_type,
    validate_required_text,
    validate_unique_id
)


def valid_client(record_id=1):
    """
    Return a valid Client record for validator tests.

    @param record_id: Client ID value to use.
    @return: Dictionary containing a valid Client record.
    """
    return {
        "ID": record_id,
        "Type": "Client",
        "Name": "Anna Kowalska",
        "Address Line 1": "1 George Street",
        "Address Line 2": "",
        "Address Line 3": "",
        "City": "Luton",
        "State": "Bedfordshire",
        "Zip Code": "LU1 1XX",
        "Country": "UK",
        "Phone Number": "07123456789"
    }


def valid_airline(record_id=1):
    """
    Return a valid Airline record for validator tests.

    @param record_id: Airline ID value to use.
    @return: Dictionary containing a valid Airline record.
    """
    return {
        "ID": record_id,
        "Type": "Airline",
        "Company Name": "British Airways"
    }


def valid_flight(record_id=1, client_id=1, airline_id=1):
    """
    Return a valid Flight record for validator tests.

    @param record_id: Flight_ID value to use.
    @param client_id: Client_ID value to use.
    @param airline_id: Airline_ID value to use.
    @return: Dictionary containing a valid Flight record.
    """
    return {
        "Flight_ID": record_id,
        "Client_ID": client_id,
        "Airline_ID": airline_id,
        "Date": "26-09-18 14:30",
        "Start City": "London",
        "End City": "Paris"
    }


def sample_records():
    """
    Return records needed to validate Flight references.

    @return: List containing one Client and one Airline record.
    """
    return [
        valid_client(1),
        valid_airline(1)
    ]


def sample_records_with_flight():
    """
    Return sample records including one Flight record.

    @return: List containing valid Client, Airline and Flight records.
    """
    return [
        valid_client(1),
        valid_airline(1),
        valid_flight(1)
    ]


def test_validate_id_accepts_positive_integer():
    """
    Check that a positive integer is accepted as a valid ID.

    @return: None.
    """
    assert validate_id(1)


@pytest.mark.parametrize("record_id", [0, -1, "1", None, True])
def test_validate_id_rejects_invalid_values(record_id):
    """
    Check that invalid ID values are rejected.

    @param record_id: Invalid ID value to check.
    @return: None.
    """
    assert not validate_id(record_id)


@pytest.mark.parametrize("record_type", ["Client", "Airline", "Flight"])
def test_validate_record_type_accepts_required_types(record_type):
    """
    Check that each required record type is accepted.

    @param record_type: Required record type to check.
    @return: None.
    """
    assert validate_record_type(record_type)


@pytest.mark.parametrize(
    "record_type", ["Hotel", "", " ", None, 1, True, [], {}]
)
def test_validate_record_type_rejects_invalid_values(record_type):
    """
    Check that unsupported record type values are rejected.

    @param record_type: Invalid record type to check.
    @return: None.
    """
    assert not validate_record_type(record_type)


@pytest.mark.parametrize(
    "record, expected_type",
    [
        (valid_client(), "Client"),
        (valid_airline(), "Airline"),
        (valid_flight(), "Flight"),
        ({"ID": 9}, None)
    ]
)
def test_record_type_for_returns_expected_type(record, expected_type):
    """
    Check that record types are identified correctly.

    @param record: Record dictionary to inspect.
    @param expected_type: Expected record type result.
    @return: None.
    """
    assert record_type_for(record) == expected_type


@pytest.mark.parametrize(
    "record, expected_id",
    [
        (valid_client(2), 2),
        (valid_airline(3), 3),
        (valid_flight(4), 4)
    ]
)
def test_record_id_for_returns_expected_id(record, expected_id):
    """
    Check that the correct ID field is used for each record type.

    @param record: Record dictionary to inspect.
    @param expected_id: Expected ID value.
    @return: None.
    """
    assert record_id_for(record) == expected_id


def test_validate_unique_id_accepts_id_when_records_empty():
    """
    Check that an ID is unique when there are no records.

    @return: None.
    """
    assert validate_unique_id([], 1, record_type="Client")


def test_validate_unique_id_accepts_new_id_for_existing_type():
    """
    Check that a new ID is accepted for an existing record type.

    @return: None.
    """
    records = sample_records()

    assert validate_unique_id(records, 2, record_type="Client")


@pytest.mark.parametrize(
    "record_type",
    ["Client", "Airline", "Flight"]
)
def test_validate_unique_id_rejects_existing_id_for_type(record_type):
    """
    Check that duplicate IDs are rejected within the same type.

    @param record_type: Record type to check for uniqueness.
    @return: None.
    """
    records = sample_records_with_flight()

    assert not validate_unique_id(records, 1, record_type=record_type)


def test_validate_unique_id_accepts_same_id_across_types():
    """
    Check that matching numeric IDs may exist across different types.

    @return: None.
    """
    records = [valid_client(1)]

    assert validate_unique_id(records, 1, record_type="Airline")


def test_validate_unique_id_accepts_current_id_on_update():
    """
    Check that a record may keep its own ID during update.

    @return: None.
    """
    records = sample_records()

    assert validate_unique_id(
        records,
        1,
        current_id=1,
        record_type="Client"
    )


@pytest.mark.parametrize(
    "records, client_id",
    [
        ([valid_client(1)], 1),
        ([valid_airline(1), valid_client(3)], 3)
    ]
)
def test_client_exists_finds_existing_client(records, client_id):
    """
    Check that existing Client records can be found by ID.

    @param records: Records list to search.
    @param client_id: Client ID to find.
    @return: None.
    """
    assert client_exists(records, client_id)


@pytest.mark.parametrize(
    "records, client_id",
    [
        ([valid_airline(1)], 1),
        ([valid_client(1)], 99)
    ]
)
def test_client_exists_rejects_missing_or_wrong_type(records, client_id):
    """
    Check that missing and non-Client records are rejected.

    @param records: Records list to search.
    @param client_id: Client ID to check.
    @return: None.
    """
    assert not client_exists(records, client_id)


@pytest.mark.parametrize(
    "records, airline_id",
    [
        ([valid_airline(1)], 1),
        ([valid_client(1), valid_airline(3)], 3)
    ]
)
def test_airline_exists_finds_existing_airline(records, airline_id):
    """
    Check that existing Airline records can be found by ID.

    @param records: Records list to search.
    @param airline_id: Airline ID to find.
    @return: None.
    """
    assert airline_exists(records, airline_id)


@pytest.mark.parametrize(
    "records, airline_id",
    [
        ([valid_client(1)], 1),
        ([valid_airline(1)], 99)
    ]
)
def test_airline_exists_rejects_missing_or_wrong_type(records, airline_id):
    """
    Check that missing and non-Airline records are rejected.

    @param records: Records list to search.
    @param airline_id: Airline ID to check.
    @return: None.
    """
    assert not airline_exists(records, airline_id)


def test_validate_date_accepts_two_digit_year_format():
    """
    Check that the agreed YY-MM-DD HH:MM date format is accepted.

    @return: None.
    """
    assert validate_date("26-09-18 14:30")


@pytest.mark.parametrize(
    "date_string",
    [
        "2026-09-18 14:30",
        "26-02-30 14:30",
        "26-09-18",
        None
    ]
)
def test_validate_date_rejects_invalid_values(date_string):
    """
    Check that invalid date values and formats are rejected.

    @param date_string: Invalid date value to check.
    @return: None.
    """
    assert not validate_date(date_string)


def test_validate_client_record_accepts_valid_client():
    """
    Check that a complete valid Client record is accepted.

    @return: None.
    """
    assert validate_client_record(valid_client())


@pytest.mark.parametrize("field", ["Address Line 2", "Address Line 3"])
def test_validate_client_record_allows_empty_optional_address(field):
    """
    Check that optional Client address lines may be empty strings.

    @param field: Optional address field to check.
    @return: None.
    """
    record = valid_client()
    record[field] = ""

    assert validate_client_record(record)


@pytest.mark.parametrize(
    "field",
    [
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
)
def test_validate_client_record_rejects_missing_fields(field):
    """
    Check that missing Client fields are rejected.

    @param field: Client field to remove.
    @return: None.
    """
    record = valid_client()
    del record[field]

    assert not validate_client_record(record)


@pytest.mark.parametrize(
    "field",
    [
        "Name",
        "Address Line 1",
        "City",
        "State",
        "Zip Code",
        "Country",
        "Phone Number"
    ]
)
def test_validate_client_record_rejects_blank_required_values(field):
    """
    Check that blank required Client values are rejected.

    @param field: Required Client field to blank.
    @return: None.
    """
    record = valid_client()
    record[field] = ""

    assert not validate_client_record(record)


@pytest.mark.parametrize("field", ["Address Line 2", "Address Line 3"])
def test_validate_client_record_rejects_non_string_address(field):
    """
    Check that optional Client address fields must be strings.

    @param field: Optional address field to change.
    @return: None.
    """
    record = valid_client()
    record[field] = None

    assert not validate_client_record(record)


@pytest.mark.parametrize("record_id", [0, "1", True])
def test_validate_client_record_rejects_invalid_id(record_id):
    """
    Check that Client records require a valid positive integer ID.

    @param record_id: Invalid Client ID value to check.
    @return: None.
    """
    record = valid_client(record_id)

    assert not validate_client_record(record)


def test_validate_client_record_rejects_wrong_type():
    """
    Check that Client-shaped data with the wrong Type is rejected.

    @return: None.
    """
    record = valid_client()
    record["Type"] = "Airline"

    assert not validate_client_record(record)


def test_validate_airline_record_accepts_company_name():
    """
    Check that an Airline record using Company Name is accepted.

    @return: None.
    """
    assert validate_airline_record(valid_airline())


def test_validate_airline_record_rejects_missing_company_name():
    """
    Check that Airline records must include Company Name.

    @return: None.
    """
    record = valid_airline()
    del record["Company Name"]

    assert not validate_airline_record(record)


def test_validate_airline_record_rejects_old_airline_name_field():
    """
    Check that the old Airline Name field is not accepted.

    @return: None.
    """
    record = {
        "ID": 1,
        "Type": "Airline",
        "Airline Name": "British Airways"
    }

    assert not validate_airline_record(record)


def test_validate_airline_record_rejects_empty_company_name():
    """
    Check that a blank Company Name is rejected.

    @return: None.
    """
    record = valid_airline()
    record["Company Name"] = ""

    assert not validate_airline_record(record)


@pytest.mark.parametrize("record_id", [0, "1", True])
def test_validate_airline_record_rejects_invalid_id(record_id):
    """
    Check that Airline records require a valid positive integer ID.

    @param record_id: Invalid Airline ID value to check.
    @return: None.
    """
    record = valid_airline(record_id)

    assert not validate_airline_record(record)


def test_validate_airline_record_rejects_wrong_type():
    """
    Check that Airline data with the wrong Type is rejected.

    @return: None.
    """
    record = valid_airline()
    record["Type"] = "Client"

    assert not validate_airline_record(record)


def test_validate_flight_record_accepts_gui_style_flight():
    """
    Check that a Flight record matching the GUI format is accepted.

    @return: None.
    """
    assert validate_flight_record(valid_flight(), sample_records())


def test_validate_flight_record_accepts_optional_type_flight():
    """
    Check that Type Flight is allowed when present.

    @return: None.
    """
    record = valid_flight()
    record["Type"] = "Flight"

    assert validate_flight_record(record, sample_records())


@pytest.mark.parametrize(
    "field",
    [
        "Flight_ID",
        "Client_ID",
        "Airline_ID",
        "Date",
        "Start City",
        "End City"
    ]
)
def test_validate_flight_record_rejects_missing_fields(field):
    """
    Check that missing Flight fields are rejected.

    @param field: Flight field to remove.
    @return: None.
    """
    record = valid_flight()
    del record[field]

    assert not validate_flight_record(record, sample_records())


def test_validate_flight_record_rejects_old_field_names():
    """
    Check that old Flight field names are rejected.

    @return: None.
    """
    record = {
        "ID": 3,
        "Type": "Flight",
        "Client_ID": 1,
        "Airline_ID": 1,
        "Date": "26-09-18 14:30",
        "Departure": "London",
        "Arrival": "Paris"
    }

    assert not validate_flight_record(record, sample_records())


@pytest.mark.parametrize(
    "field, value",
    [
        ("Client_ID", 99),
        ("Airline_ID", 99)
    ]
)
def test_validate_flight_record_rejects_missing_references(field, value):
    """
    Check that Flight records must reference existing records.

    @param field: Flight reference field to change.
    @param value: Missing reference ID to use.
    @return: None.
    """
    record = valid_flight()
    record[field] = value

    assert not validate_flight_record(record, sample_records())


@pytest.mark.parametrize(
    "field, value",
    [
        ("Client_ID", "1"),
        ("Airline_ID", "1"),
        ("Client_ID", 0),
        ("Airline_ID", -1),
        ("Client_ID", True),
        ("Airline_ID", True)
    ]
)
def test_validate_flight_record_rejects_invalid_reference_ids(field, value):
    """
    Check that Flight reference IDs must be positive integers.

    @param field: Flight reference ID field to change.
    @param value: Invalid reference ID value to use.
    @return: None.
    """
    record = valid_flight()
    record[field] = value

    assert not validate_flight_record(record, sample_records())


@pytest.mark.parametrize(
    "date_string",
    [
        "2026-09-18 14:30",
        "26-02-30 14:30",
        None
    ]
)
def test_validate_flight_record_rejects_invalid_dates(date_string):
    """
    Check that Flight records require a valid date value.

    @param date_string: Invalid date value to use.
    @return: None.
    """
    record = valid_flight()
    record["Date"] = date_string

    assert not validate_flight_record(record, sample_records())


@pytest.mark.parametrize("field", ["Start City", "End City"])
def test_validate_flight_record_rejects_blank_city_values(field):
    """
    Check that Flight city fields cannot be blank.

    @param field: Flight city field to blank.
    @return: None.
    """
    record = valid_flight()
    record[field] = ""

    assert not validate_flight_record(record, sample_records())


def test_validate_flight_record_rejects_wrong_type():
    """
    Check that a Flight record with the wrong Type is rejected.

    @return: None.
    """
    record = valid_flight()
    record["Type"] = "Client"

    assert not validate_flight_record(record, sample_records())


@pytest.mark.parametrize(
    "record, records",
    [
        (valid_client(2), sample_records()),
        (valid_airline(2), sample_records()),
        (valid_flight(1), sample_records())
    ]
)
def test_validate_record_accepts_valid_records(record, records):
    """
    Check that the general validator accepts valid records.

    @param record: Valid record to check.
    @param records: Existing records list to validate against.
    @return: None.
    """
    assert validate_record(record, records)


def test_validate_record_rejects_missing_type_for_non_flight():
    """
    Check that non-Flight records require a Type field.

    @return: None.
    """
    record = valid_client()
    del record["Type"]

    assert not validate_record(record, [])


def test_validate_record_rejects_invalid_type():
    """
    Check that unsupported record types are rejected.

    @return: None.
    """
    record = valid_client()
    record["Type"] = "Hotel"

    assert not validate_record(record, [])


def test_validate_record_rejects_missing_client_id_field():
    """
    Check that Client records require the ID field.

    @return: None.
    """
    record = valid_client()
    del record["ID"]

    assert not validate_record(record, [])


def test_validate_record_rejects_missing_flight_id_field():
    """
    Check that Flight records require the Flight_ID field.

    @return: None.
    """
    record = valid_flight()
    record["Type"] = "Flight"
    del record["Flight_ID"]

    assert not validate_record(record, sample_records())


@pytest.mark.parametrize(
    "record",
    [
        valid_client(1),
        valid_airline(1),
        valid_flight(1)
    ]
)
def test_validate_record_rejects_duplicate_id_within_type(record):
    """
    Check that duplicate IDs are rejected within the same type.

    @param record: Record with a duplicate ID.
    @return: None.
    """
    records = sample_records_with_flight()

    assert not validate_record(record, records)


def test_validate_record_allows_same_id_across_different_types():
    """
    Check that the same numeric ID may exist across types.

    @return: None.
    """
    records = [valid_client(1)]

    assert validate_record(valid_airline(1), records)


@pytest.mark.parametrize("record_type", [None, "", "Hotel", [], {}])
def test_record_type_for_rejects_explicit_invalid_flight_type(record_type):
    """
    Check that an invalid Type does not trigger Flight inference.

    @param record_type: Explicit invalid Type value.
    @return: None.
    """
    record = valid_flight()
    record["Type"] = record_type

    assert record_type_for(record) is None


@pytest.mark.parametrize("record_type", [None, "", "Hotel", [], {}])
@pytest.mark.parametrize(
    "validator", [validate_flight_record, validate_record]
)
def test_flight_validators_reject_explicit_invalid_type(
    validator, record_type
):
    """
    Check that Flight validators reject an explicitly invalid Type.

    @param validator: Record validation function to check.
    @param record_type: Explicit invalid Type value.
    @return: None.
    """
    record = valid_flight()
    record["Type"] = record_type

    assert not validator(record, sample_records())


@pytest.mark.parametrize("record", [None, [], "Flight", 1])
@pytest.mark.parametrize("helper", [record_type_for, record_id_for])
def test_record_helpers_handle_non_dictionary_values(helper, record):
    """
    Check that record helpers safely return None for non-dictionaries.

    @param helper: Record helper function to check.
    @param record: Invalid record value.
    @return: None.
    """
    assert helper(record) is None


@pytest.mark.parametrize("record", [None, [], "Client", 1])
@pytest.mark.parametrize(
    "validator", [validate_client_record, validate_airline_record]
)
def test_single_record_validators_reject_non_dictionaries(validator, record):
    """
    Check that Client and Airline validators reject non-dictionaries.

    @param validator: Record validation function to check.
    @param record: Invalid record value.
    @return: None.
    """
    assert not validator(record)


@pytest.mark.parametrize("record", [None, [], "Flight", 1])
@pytest.mark.parametrize(
    "validator", [validate_flight_record, validate_record]
)
def test_validators_with_records_reject_non_dictionaries(validator, record):
    """
    Check that Flight and general validators reject non-dictionaries.

    @param validator: Record validation function to check.
    @param record: Invalid record value.
    @return: None.
    """
    assert not validator(record, sample_records())


@pytest.mark.parametrize(
    "date_string",
    [
        "26-9-18 14:30",
        "26-09-8 14:30",
        "26-09-18 4:30",
        "26-09-18 14:3",
        " 26-09-18 14:30",
        "26-09-18 14:30 ",
        "26-09-18  14:30",
        "26-09-18\t14:30",
        "26-09-18 14:30\n"
    ]
)
def test_validate_date_rejects_non_strict_format(date_string):
    """
    Check padding and exact whitespace in the agreed date format.

    @param date_string: Date with invalid padding or whitespace.
    @return: None.
    """
    assert not validate_date(date_string)


@pytest.mark.parametrize(
    "date_string", ["24-02-29 00:00", "26-09-18 23:59"]
)
def test_validate_date_accepts_leap_day_and_time_boundaries(date_string):
    """
    Check a valid leap day, midnight and the last minute of the day.

    @param date_string: Valid date and time to check.
    @return: None.
    """
    assert validate_date(date_string)


@pytest.mark.parametrize(
    "date_string",
    ["26-02-29 14:30", "26-09-18 24:00", "26-09-18 14:60"]
)
def test_validate_date_rejects_invalid_calendar_and_time(date_string):
    """
    Check an invalid leap day and out-of-range hours and minutes.

    @param date_string: Invalid date and time to check.
    @return: None.
    """
    assert not validate_date(date_string)


@pytest.mark.parametrize("value", ["London", " London "])
def test_validate_required_text_accepts_non_blank_strings(value):
    """
    Check that required text accepts strings containing visible text.

    @param value: Valid required text value.
    @return: None.
    """
    assert validate_required_text(value)


@pytest.mark.parametrize("value", ["", "   ", "\t\n", None, 123, True])
def test_validate_required_text_rejects_invalid_values(value):
    """
    Check that required text rejects blank and non-string values.

    @param value: Invalid required text value.
    @return: None.
    """
    assert not validate_required_text(value)


@pytest.mark.parametrize("value", ["Flat 2", "", "   "])
def test_validate_optional_text_accepts_strings(value):
    """
    Check that optional text accepts strings, including blank strings.

    @param value: Valid optional text value.
    @return: None.
    """
    assert validate_optional_text(value)


@pytest.mark.parametrize("value", [None, 123, True, [], {}])
def test_validate_optional_text_rejects_non_strings(value):
    """
    Check that optional text still requires a string value.

    @param value: Invalid optional text value.
    @return: None.
    """
    assert not validate_optional_text(value)


@pytest.mark.parametrize(
    "record_factory, record_type",
    [
        (valid_client, "Client"),
        (valid_airline, "Airline"),
        (valid_flight, "Flight")
    ]
)
def test_validate_unique_id_rejects_occupied_id_on_update(
    record_factory, record_type
):
    """
    Check that an update cannot reuse an ID occupied within its type.

    @param record_factory: Helper creating a valid record of this type.
    @param record_type: Type whose ID uniqueness is checked.
    @return: None.
    """
    records = [record_factory(1), record_factory(2)]

    assert not validate_unique_id(
        records, 2, current_id=1, record_type=record_type
    )


@pytest.mark.parametrize(
    "record_factory", [valid_client, valid_airline, valid_flight]
)
def test_validate_record_rejects_occupied_id_on_update(record_factory):
    """
    Check that general validation rejects an update to an occupied ID.

    @param record_factory: Helper creating a valid record of this type.
    @return: None.
    """
    records = sample_records_with_flight()
    records.append(record_factory(2))
    updated_record = record_factory(2)

    assert not validate_record(updated_record, records, current_id=1)


@pytest.mark.parametrize("record_id", [0, -1, "1", None, True, 1.5])
def test_validate_flight_record_rejects_invalid_flight_id(record_id):
    """
    Check that a Flight ID must be a positive non-boolean integer.

    @param record_id: Invalid Flight ID value to check.
    @return: None.
    """
    record = valid_flight(record_id)

    assert not validate_flight_record(record, sample_records())


@pytest.mark.parametrize("record_id", [0, -1, "1", None, True, 1.5])
@pytest.mark.parametrize(
    "record_factory", [valid_client, valid_airline, valid_flight]
)
def test_validate_record_rejects_invalid_id(record_factory, record_id):
    """
    Check that general validation rejects invalid IDs for every type.

    @param record_factory: Helper creating a valid record of this type.
    @param record_id: Invalid record ID value to check.
    @return: None.
    """
    record = record_factory(record_id)

    assert not validate_record(record, sample_records())


def test_validate_record_rejects_type_without_handler(monkeypatch):
    """
    Check the defensive fallback for an allowed type without a handler.

    This path is unreachable with the current supported types. Adding
    Hotel temporarily simulates a new allowed type without a validation
    handler. Pytest restores VALID_TYPES after this test.

    @param monkeypatch: Pytest fixture for temporary attribute changes.
    @return: None.
    """
    monkeypatch.setattr(
        validators, "VALID_TYPES", validators.VALID_TYPES | {"Hotel"}
    )
    record = {"ID": 1, "Type": "Hotel"}

    assert not validate_record(record, [])
