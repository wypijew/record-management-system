from validators import (
    validate_id,
    validate_record_type,
    validate_unique_id,
    client_exists,
    airline_exists,
    validate_client_record,
    validate_airline_record,
    validate_flight_record,
    validate_record,
)


def test_validate_id_accepts_positive_integer():
    # Verify that a positive integer is accepted as a valid ID.
    assert validate_id(1) is True


def test_validate_id_rejects_zero():
    # Verify that zero is rejected because IDs must be positive.
    assert validate_id(0) is False


def test_validate_id_rejects_negative_integer():
    # Verify that a negative integer is rejected as an invalid ID.
    assert validate_id(-1) is False


def test_validate_id_rejects_string():
    # Verify that a string is rejected because IDs must be integers.
    assert validate_id('1') is False


def test_validate_id_rejects_none():
    # Verify that None is rejected as an invalid ID.
    assert validate_id(None) is False


def test_validate_record_type_accepts_client():
    # Verify that Client is accepted as a supported record type.
    assert validate_record_type('Client') is True


def test_validate_record_type_accepts_airline():
    # Verify that Airline is accepted as a supported record type.
    assert validate_record_type('Airline') is True


def test_validate_record_type_accepts_flight():
    # Verify that Flight is accepted as a supported record type.
    assert validate_record_type('Flight') is True


def test_validate_record_type_rejects_invalid_type():
    # Verify that an unsupported record type is rejected.
    assert validate_record_type('Hotel') is False


def test_validate_record_type_rejects_blank_type():
    # Verify that a blank record type is rejected.
    assert validate_record_type(' ') is False


def test_validate_record_type_rejects_none():
    # Verify that None is rejected as a record type.
    assert validate_record_type(None) is False


def test_validate_unique_id_accepts_id_when_records_empty():
    # Verify that an ID is unique when no records exist.
    records = [
        ]
    assert validate_unique_id(records, 1) is True


def test_validate_unique_id_rejects_existing_id():
    # Verify that an ID already present in the records is rejected.
    records = [
            {"ID": 1, "Type": "Client"},
        ]
    assert validate_unique_id(records, 1) is False


def test_validate_unique_id_accepts_new_id():
    # Verify that an unused ID is accepted.
    records = [
            {"ID": 1, "Type": "Client"},
        ]
    assert validate_unique_id(records, 2) is True


def test_validate_unique_id_accepts_current_id_on_update():
    # Verify that a record may keep its current ID during an update.
    records = [
            {"ID": 1, "Type": "Client"},
        ]
    assert validate_unique_id(records, 1, 1) is True


def test_validate_unique_id_rejects_existing_id_on_update():
    # Verify that an update cannot use an ID assigned to another record.
    records = [
            {"ID": 1, "Type": "Client"},
            {"ID": 2, "Type": "Client"},
        ]
    assert validate_unique_id(records, 2, 1) is False


def test_client_exists_returns_true_for_existing_client():
    # Verify that an existing client can be found by ID.
    records = [
            {"ID": 1, "Type": "Client"},
        ]
    assert client_exists(records, 1) is True


def test_client_exists_returns_false_for_missing_client():
    # Verify that a missing client returns False.
    records = [
            {"ID": 1, "Type": "Client"},
        ]
    assert client_exists(records, 2) is False


def test_client_exists_finds_client_later_in_list():
    # Verify that the search checks records beyond the first list item.
    records = [
            {"ID": 1, "Type": "Client"},
            {"ID": 2, "Type": "Client"},
            {"ID": 3, "Type": "Client"},
        ]
    # Currently fails because client_exists() returns False
    # before checking all records in the list.
    assert client_exists(records, 3) is True


def test_client_exists_rejects_non_client_record():
    # Verify that a matching ID is rejected for a non-Client record.
    records = [
            {"ID": 1, "Type": "Airline"},
        ]
    assert client_exists(records, 1) is False


def test_airline_exists_returns_true_for_existing_airline():
    # Verify that an existing airline can be found by ID.
    records = [
            {"ID": 1, "Type": "Airline"},
        ]
    assert airline_exists(records, 1) is True


def test_airline_exists_returns_false_for_missing_airline():
    # Verify that a missing airline returns False.
    records = [
            {"ID": 1, "Type": "Airline"},
        ]
    assert airline_exists(records, 2) is False


def test_airline_exists_finds_airline_later_in_list():
    # Verify that the airline search checks the full records list.
    records = [
            {"ID": 1, "Type": "Airline"},
            {"ID": 2, "Type": "Airline"},
            {"ID": 3, "Type": "Airline"},
        ]
    assert airline_exists(records, 3) is True


def test_airline_exists_rejects_non_airline_record():
    # Verify that a matching ID is rejected for a non-Airline record.
    records = [
            {"ID": 1, "Type": "Client"},
        ]
    assert airline_exists(records, 1) is False


def test_validate_client_record_accepts_valid_client():
    # Verify that a complete valid client record is accepted.
    record = {
            "ID": 1,
            "Type": "Client",
            "Name": "Anna Kowalska",
            "Address Line 1": "1 George Street",
            "City": "Luton",
            "State": "Bedfordshire",
            "Zip Code": "LU1 1XX",
            "Country": "UK",
            "Phone Number": "07123456789",
        }
    # The required fields currently contain "Number" instead of
    # "Phone Number", which may cause a valid client record to be rejected.
    assert validate_client_record(record) is True


def test_validate_client_record_rejects_missing_name():
    # Verify that a client record without Name is rejected.
    record = {
            "ID": 1,
            "Type": "Client",
            "Address Line 1": "1 George Street",
            "City": "Luton",
            "State": "Bedfordshire",
            "Zip Code": "LU1 1XX",
            "Country": "UK",
            "Phone Number": "07123456789",
        }
    assert validate_client_record(record) is False


def test_validate_client_record_rejects_empty_name():
    # Verify that a blank client Name is rejected.
    record = {
            "ID": 1,
            "Type": "Client",
            "Name": "",
            "Address Line 1": "1 George Street",
            "City": "Luton",
            "State": "Bedfordshire",
            "Zip Code": "LU1 1XX",
            "Country": "UK",
            "Phone Number": "07123456789",
        }
    assert validate_client_record(record) is False


def test_validate_client_record_rejects_empty_city():
    # Verify that a blank City is rejected.
    record = {
            "ID": 1,
            "Type": "Client",
            "Name": "Anna Kowalska",
            "Address Line 1": "1 George Street",
            "City": "",
            "State": "Bedfordshire",
            "Zip Code": "LU1 1XX",
            "Country": "UK",
            "Phone Number": "07123456789",
        }
    assert validate_client_record(record) is False


def test_validate_client_record_rejects_empty_state():
    # Verify that a blank State is rejected.
    record = {
            "ID": 1,
            "Type": "Client",
            "Name": "Anna Kowalska",
            "Address Line 1": "1 George Street",
            "City": "Luton",
            "State": "",
            "Zip Code": "LU1 1XX",
            "Country": "UK",
            "Phone Number": "07123456789",
        }
    assert validate_client_record(record) is False


def test_validate_client_record_rejects_empty_zip_code():
    # Verify that a blank Zip Code is rejected.
    record = {
            "ID": 1,
            "Type": "Client",
            "Name": "Anna Kowalska",
            "Address Line 1": "1 George Street",
            "City": "Luton",
            "State": "Bedfordshire",
            "Zip Code": "",
            "Country": "UK",
            "Phone Number": "07123456789",
        }
    # The Zip Code validation currently contains "Flase" instead of "False".
    assert validate_client_record(record) is False


def test_validate_client_record_rejects_empty_country():
    # Verify that a blank Country is rejected.
    record = {
            "ID": 1,
            "Type": "Client",
            "Name": "Anna Kowalska",
            "Address Line 1": "1 George Street",
            "City": "Luton",
            "State": "Bedfordshire",
            "Zip Code": "LU1 1XX",
            "Country": "",
            "Phone Number": "07123456789",
        }
    assert validate_client_record(record) is False


def test_validate_client_record_rejects_empty_phone_number():
    # Verify that a blank Phone Number is rejected.
    record = {
            "ID": 1,
            "Type": "Client",
            "Name": "Anna Kowalska",
            "Address Line 1": "1 George Street",
            "City": "Luton",
            "State": "Bedfordshire",
            "Zip Code": "LU1 1XX",
            "Country": "UK",
            "Phone Number": "",
        }
    assert validate_client_record(record) is False


def test_validate_client_record_rejects_wrong_type():
    # Verify that client data with the wrong record Type is rejected.
    record = {
            "ID": 1,
            "Type": "Airline",
            "Name": "Anna Kowalska",
            "Address Line 1": "1 George Street",
            "City": "Luton",
            "State": "Bedfordshire",
            "Zip Code": "LU1 1XX",
            "Country": "UK",
            "Phone Number": "07123456789",
        }
    assert validate_client_record(record) is False


def test_validate_airline_record_accepts_valid_airline():
    # Verify that a complete valid airline record is accepted.
    record = {
            "ID": 1,
            "Type": "Airline",
            "Airline Name": "British Airways",
        }
    assert validate_airline_record(record) is True


def test_validate_airline_record_rejects_missing_name():
    # Verify that an airline record without Airline Name is rejected.
    record = {
            "ID": 1,
            "Type": "Airline",
        }
    assert validate_airline_record(record) is False


def test_validate_airline_record_rejects_empty_name():
    # Verify that a blank Airline Name is rejected.
    record = {
            "ID": 1,
            "Type": "Airline",
            "Airline Name": "",
        }
    assert validate_airline_record(record) is False


def test_validate_airline_record_rejects_wrong_type():
    # Verify that airline data with the wrong record Type is rejected.
    record = {
            "ID": 1,
            "Type": "Client",
            "Airline Name": "British Airways",
        }
    assert validate_airline_record(record) is False


def test_validate_flight_record_accepts_valid_flight():
    # Verify that a complete valid flight record is accepted.
    records = [
            {"ID": 1, "Type": "Client"},
            {"ID": 2, "Type": "Airline"},
        ]
    record = {
            "ID": 3,
            "Type": "Flight",
            "Client_ID": 1,
            "Airline_ID": 2,
            "Date": "2026-09-14 14:00",
            "Departure": "London",
            "Arrival": "Paris",
        }
    # The validator currently checks for "Flgiht" instead of "Flight",
    # which may cause a valid flight record to be rejected.
    assert validate_flight_record(record, records) is True


def test_validate_flight_record_rejects_missing_client_id():
    # Verify that a flight without Client_ID is rejected.
    records = [
            {"ID": 1, "Type": "Client"},
            {"ID": 2, "Type": "Airline"},
        ]
    record = {
            "ID": 3,
            "Type": "Flight",
            "Airline_ID": 2,
            "Date": "2026-09-14 14:00",
            "Departure": "London",
            "Arrival": "Paris",
        }
    assert validate_flight_record(record, records) is False


def test_validate_flight_record_rejects_missing_airline_id():
    # Verify that a flight without Airline_ID is rejected.
    records = [
            {"ID": 1, "Type": "Client"},
            {"ID": 2, "Type": "Airline"},
        ]
    record = {
            "ID": 3,
            "Type": "Flight",
            "Client_ID": 1,
            "Date": "2026-09-14 14:00",
            "Departure": "London",
            "Arrival": "Paris",
        }
    assert validate_flight_record(record, records) is False


def test_validate_flight_record_rejects_nonexistent_client():
    # Verify that a flight cannot reference a missing client.
    records = [
            {"ID": 1, "Type": "Client"},
            {"ID": 2, "Type": "Airline"},
        ]
    record = {
            "ID": 3,
            "Type": "Flight",
            "Client_ID": 5,
            "Airline_ID": 2,
            "Date": "2026-09-14 14:00",
            "Departure": "London",
            "Arrival": "Paris",
        }
    assert validate_flight_record(record, records) is False


def test_validate_flight_record_rejects_nonexistent_airline():
    # Verify that a flight cannot reference a missing airline.
    records = [
            {"ID": 1, "Type": "Client"},
            {"ID": 2, "Type": "Airline"},
        ]
    record = {
            "ID": 3,
            "Type": "Flight",
            "Client_ID": 1,
            "Airline_ID": 5,
            "Date": "2026-09-14 14:00",
            "Departure": "London",
            "Arrival": "Paris",
        }
    assert validate_flight_record(record, records) is False


def test_validate_flight_record_rejects_client_id_as_string():
    # Verify that Client_ID is rejected when supplied as a string.
    records = [
            {"ID": 1, "Type": "Client"},
            {"ID": 2, "Type": "Airline"},
        ]
    record = {
            "ID": 3,
            "Type": "Flight",
            "Client_ID": "1",
            "Airline_ID": 2,
            "Date": "2026-09-14 14:00",
            "Departure": "London",
            "Arrival": "Paris",
        }
    assert validate_flight_record(record, records) is False


def test_validate_flight_record_rejects_airline_id_as_string():
    # Verify that Airline_ID is rejected when supplied as a string.
    records = [
            {"ID": 1, "Type": "Client"},
            {"ID": 2, "Type": "Airline"},
        ]
    record = {
            "ID": 3,
            "Type": "Flight",
            "Client_ID": 1,
            "Airline_ID": "2",
            "Date": "2026-09-14 14:00",
            "Departure": "London",
            "Arrival": "Paris",
        }
    assert validate_flight_record(record, records) is False


def test_validate_flight_record_rejects_empty_departure():
    # Verify that a flight with a blank Departure is rejected.
    records = [
            {"ID": 1, "Type": "Client"},
            {"ID": 2, "Type": "Airline"},
        ]
    record = {
            "ID": 3,
            "Type": "Flight",
            "Client_ID": 1,
            "Airline_ID": 2,
            "Date": "2026-09-14 14:00",
            "Departure": "",
            "Arrival": "Paris",
        }
    assert validate_flight_record(record, records) is False


def test_validate_flight_record_rejects_empty_arrival():
    # Verify that a flight with a blank Arrival is rejected.
    records = [
            {"ID": 1, "Type": "Client"},
            {"ID": 2, "Type": "Airline"},
        ]
    record = {
            "ID": 3,
            "Type": "Flight",
            "Client_ID": 1,
            "Airline_ID": 2,
            "Date": "2026-09-14 14:00",
            "Departure": "London",
            "Arrival": "",
        }
    assert validate_flight_record(record, records) is False


def test_validate_flight_record_rejects_wrong_type():
    # Verify that flight data with the wrong record Type is rejected.
    records = [
            {"ID": 1, "Type": "Client"},
            {"ID": 2, "Type": "Airline"},
        ]
    record = {
            "ID": 3,
            "Type": "Client",
            "Client_ID": 1,
            "Airline_ID": 2,
            "Date": "2026-09-14 14:00",
            "Departure": "London",
            "Arrival": "Paris",
        }
    assert validate_flight_record(record, records) is False


def test_validate_record_rejects_missing_type():
    # Verify that the main validator rejects a record without Type.
    records = [
        ]
    record = {
            "ID": 1,
            "Name": "Anna Kowalska",
        }
    assert validate_record(record, records) is False


def test_validate_record_rejects_invalid_type():
    # Verify that the main validator rejects an unsupported Type.
    records = [
        ]
    record = {
            "ID": 1,
            "Type": "Hotel",
        }
    assert validate_record(record, records) is False


def test_validate_record_rejects_missing_id():
    # Verify that the main validator rejects a record without ID.
    records = [
        ]
    record = {
            "Type": "Client",
            "Name": "Anna Kowalska",
            "Address Line 1": "1 George Street",
            "City": "Luton",
            "State": "Bedfordshire",
            "Zip Code": "LU1 1XX",
            "Country": "UK",
            "Phone Number": "07123456789",
        }
    assert validate_record(record, records) is False


def test_validate_record_rejects_duplicate_id():
    # Verify that the main validator rejects a duplicate ID.
    records = [
            {"ID": 1, "Type": "Client"},
        ]
    record = {
            "ID": 1,
            "Type": "Client",
            "Name": "Anna Kowalska",
            "Address Line 1": "1 George Street",
            "City": "Luton",
            "State": "Bedfordshire",
            "Zip Code": "LU1 1XX",
            "Country": "UK",
            "Phone Number": "07123456789",
        }
    assert validate_record(record, records) is False
