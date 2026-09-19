"""Unit tests for creating, finding, updating and deleting records."""

import pytest

from models import make_airline_record, make_client_record, make_flight_record
from record_manager import (
    create_record,
    delete_record,
    find_record_by_id,
    get_records_by_type,
    id_exists,
    search_records,
    update_record,
)


def make_records():
    """
    Create a valid set of Client, Airline and Flight records.

    @return: List containing two Clients, one Airline and one Flight.
    """
    client_one = make_client_record(
        1, "Anna Kowalska", "12 High Street", "", "", "Luton",
        "Bedfordshire", "LU1 1XX", "UK", "07123456789"
    )
    client_two = make_client_record(
        2, "Jan Nowak", "34 Market Road", "", "", "London",
        "London", "E1 6AN", "UK", "07987654321"
    )
    airline = make_airline_record(1, "Example Air")
    flight = make_flight_record(
        1, 1, 1, "26-09-18 14:30", "Luton", "Paris"
    )
    return [client_one, client_two, airline, flight]


def test_id_exists_finds_an_existing_record_id():
    """
    Check that an existing numeric ID is found.

    @return: None.
    """
    records = make_records()

    assert id_exists(records, 1)


def test_id_exists_rejects_an_unknown_record_id():
    """
    Check that an unknown numeric ID is not found.

    @return: None.
    """
    records = make_records()

    assert not id_exists(records, 99)


def test_find_record_by_id_can_filter_by_record_type():
    """
    Check that records with a shared ID can be identified by type.

    @return: None.
    """
    records = make_records()

    assert find_record_by_id(records, 1, "Client") == records[0]
    assert find_record_by_id(records, 1, "Airline") == records[2]
    assert find_record_by_id(records, 1, "Flight") == records[3]


def test_find_record_by_id_returns_first_match_without_type_filter():
    """
    Check that a search without a type returns the first match.

    @return: None.
    """
    records = make_records()

    assert find_record_by_id(records, 1) == records[0]
    assert find_record_by_id(records, 99) is None


def test_find_record_by_id_rejects_an_unknown_record_type():
    """
    Check that an unknown type does not match a shared numeric ID.

    @return: None.
    """
    records = make_records()

    assert find_record_by_id(records, 1, "Hotel") is None


def test_get_records_by_type_returns_only_requested_records():
    """
    Check that a type filter returns only matching records.

    @return: None.
    """
    records = make_records()

    assert get_records_by_type(records, "Client") == records[:2]
    assert get_records_by_type(records, "Flight") == [records[3]]
    assert not get_records_by_type(records, "Hotel")


def test_search_records_supports_id_and_type_filters():
    """
    Check searches using an ID, a type and both criteria.

    @return: None.
    """
    records = make_records()

    assert search_records(records, record_id=2) == [records[1]]
    assert search_records(records, record_type="Airline") == [records[2]]
    assert search_records(records, 1, "Flight") == [records[3]]
    assert not search_records(records, 99, "Client")


def test_search_records_without_filters_returns_all_records():
    """
    Check that an unfiltered search returns every record.

    @return: None.
    """
    records = make_records()

    assert search_records(records) == records


def test_create_record_adds_a_valid_record():
    """
    Check that a valid record is added to the supplied list.

    @return: None.
    """
    records = make_records()
    new_client = make_client_record(
        3, "Maria Green", "5 Station Road", "", "", "Oxford",
        "Oxfordshire", "OX1 1AA", "UK", "07000000000"
    )

    assert create_record(records, new_client)
    assert records[-1] == new_client


def test_create_record_rejects_an_invalid_record_without_adding_it():
    """
    Check that an invalid record leaves the list unchanged.

    @return: None.
    """
    records = make_records()
    invalid_flight = make_flight_record(
        2, 99, 1, "26-09-18 14:30", "Luton", "Paris"
    )
    original_length = len(records)

    assert not create_record(records, invalid_flight)
    assert len(records) == original_length


def test_update_record_changes_a_valid_record():
    """
    Check that a valid update changes the matching record.

    @return: None.
    """
    records = make_records()

    assert update_record(records, 1, {"End City": "Rome"}, "Flight")
    assert records[3]["End City"] == "Rome"


def test_update_record_rejects_invalid_data_without_changing_record():
    """
    Check that a rejected update preserves the original record.

    @return: None.
    """
    records = make_records()
    original_flight = records[3].copy()

    assert not update_record(records, 1, {"Client_ID": 99}, "Flight")
    assert records[3] == original_flight


def test_update_record_uses_the_requested_record_type():
    """
    Check that an update affects the record of the requested type.

    @return: None.
    """
    records = make_records()
    original_client = records[0].copy()

    assert update_record(
        records, 1, {"Company Name": "Changed Air"}, "Airline"
    )
    assert records[0] == original_client
    assert records[2]["Company Name"] == "Changed Air"


def test_update_record_rejects_an_unknown_record_type():
    """
    Check that an unknown type does not update a shared ID.

    @return: None.
    """
    records = make_records()

    assert not update_record(records, 1, {"Name": "Changed"}, "Hotel")


@pytest.mark.parametrize("record_type", [None, "Flight"])
def test_delete_record_removes_the_matching_record(record_type):
    """
    Check that deleting a Flight works with and without its type.

    @param record_type: Optional type supplied to the delete operation.
    @return: None.
    """
    records = make_records()

    assert delete_record(records, 1, record_type)
    assert len(records) == 3


def test_delete_record_rejects_an_unknown_record():
    """
    Check that deleting an unknown record leaves the list unchanged.

    @return: None.
    """
    records = make_records()
    original_length = len(records)

    assert not delete_record(records, 99, "Flight")
    assert len(records) == original_length


def test_delete_record_rejects_an_unknown_type_for_an_existing_id():
    """
    Check that an unknown type does not delete a record with a shared ID.

    @return: None.
    """
    records = make_records()
    original_records = records.copy()

    assert not delete_record(records, 1, "Hotel")
    assert records == original_records
