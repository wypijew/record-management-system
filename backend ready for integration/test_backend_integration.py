"""Checks for the record format shared with the GUI."""

from models import make_airline_record, make_client_record, make_flight_record
from record_manager import (
    create_record,
    delete_record,
    search_records,
    update_record
)
from storage import load_records, save_records
from validators import validate_date


def sample_records():
    """
    Create a small valid Client and Airline dataset.

    @return: List containing one Client and one Airline record.
    """
    records = []
    client = make_client_record(1, "Alex", "Main Street", "", "", "Luton",
                                "Beds", "LU1", "UK", "12345")
    airline = make_airline_record(1, "Example Air")
    assert create_record(records, client)
    assert create_record(records, airline)
    return records


def test_gui_field_names_and_ids_are_valid():
    """
    Check that backend records match the GUI field names.

    @return: None.
    """
    records = sample_records()
    flight = make_flight_record(1, 1, 1, "26-09-18 14:30", "Luton", "Paris")
    assert create_record(records, flight)
    assert flight["Flight_ID"] == 1
    assert "Type" not in flight
    assert flight["Start City"] == "Luton"
    assert records[1]["Company Name"] == "Example Air"
    assert search_records(records, 1, "Flight") == [flight]
    assert search_records(records, 1, "Client") == [records[0]]


def test_create_rejects_missing_parent_and_duplicate_flight_id():
    """
    Check that invalid Flight creation attempts are rejected.

    @return: None.
    """
    records = sample_records()
    missing_client = make_flight_record(1, 99, 1, "26-09-18 14:30", "A", "B")
    assert not create_record(records, missing_client)
    flight = make_flight_record(1, 1, 1, "26-09-18 14:30", "A", "B")
    assert create_record(records, flight)
    assert not create_record(records, flight.copy())


def test_update_and_delete_flight_use_flight_id():
    """
    Check update and delete operations using Flight_ID.

    @return: None.
    """
    records = sample_records()
    flight = make_flight_record(5, 1, 1, "26-09-18 14:30", "A", "B")
    assert create_record(records, flight)
    assert update_record(records, 5, {"End City": "Rome"}, "Flight")
    assert search_records(records, 5, "Flight")[0]["End City"] == "Rome"
    assert not update_record(records, 5, {"Client_ID": 99}, "Flight")
    assert delete_record(records, 5, "Flight")
    assert not search_records(records, 5, "Flight")


def test_date_requires_two_digit_year():
    """
    Check that dates use the agreed YY-MM-DD HH:MM format.

    @return: None.
    """
    assert validate_date("26-09-18 14:30")
    assert not validate_date("2026-09-18 14:30")
    assert not validate_date("26-02-30 14:30")
    assert not validate_date(None)


def test_json_persistence_round_trip(tmp_path):
    """
    Check that records can be saved to and loaded from JSON.

    @param tmp_path: Temporary path fixture supplied by pytest.
    @return: None.
    """
    records = sample_records()
    filename = tmp_path / "records.json"
    assert load_records(filename) == []
    save_records(filename, records)
    assert load_records(filename) == records
