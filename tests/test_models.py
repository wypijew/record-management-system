"""Unit tests for Client, Airline and Flight record creation."""

import pytest

from models import (
    make_airline_record,
    make_client_record,
    make_flight_record
)


@pytest.mark.parametrize(
    "name, city, phone",
    [
        ("Anna Kowalska", "Luton", "07123456789"),
        ("Łukasz Żak", "Łódź", "+48 012 345 678")
    ]
)
def test_make_client_record_maps_all_fields(name, city, phone):
    """
    Check Client field names and preserve supplied text values.

    @param name: Client name, including non-ASCII characters.
    @param city: Client city to preserve.
    @param phone: Phone string whose formatting must be preserved.
    @return: None.
    """
    record = make_client_record(
        7, name, "12 High Street", "Flat 3", "North Wing", city,
        "Bedfordshire", "00123", "UK", phone
    )

    assert record == {
        "ID": 7,
        "Type": "Client",
        "Name": name,
        "Address Line 1": "12 High Street",
        "Address Line 2": "Flat 3",
        "Address Line 3": "North Wing",
        "City": city,
        "State": "Bedfordshire",
        "Zip Code": "00123",
        "Country": "UK",
        "Phone Number": phone
    }


@pytest.mark.parametrize(
    "address2, address3",
    [("", "North Wing"), ("Flat 3", ""), ("", "")]
)
def test_make_client_record_keeps_empty_optional_fields(address2, address3):
    """
    Check that empty optional address lines remain present as strings.

    @param address2: Second address line, possibly empty.
    @param address3: Third address line, possibly empty.
    @return: None.
    """
    record = make_client_record(
        7, "Anna Kowalska", "12 High Street", address2, address3,
        "Luton", "Bedfordshire", "LU1 1XX", "UK", "07123456789"
    )

    assert record["Address Line 2"] == address2
    assert record["Address Line 3"] == address3


@pytest.mark.parametrize("company_name", ["British Airways", "Łódź Air"])
def test_make_airline_record_maps_all_fields(company_name):
    """
    Check Airline schema and preserve the company name.

    @param company_name: Airline company name to preserve.
    @return: None.
    """
    record = make_airline_record(13, company_name)

    assert record == {
        "ID": 13,
        "Type": "Airline",
        "Company Name": company_name
    }


@pytest.mark.parametrize(
    "date, start_city, end_city",
    [
        ("26-09-18 14:30", "London", "Paris"),
        ("28-02-29 00:05", "Łódź", "München")
    ]
)
def test_make_flight_record_matches_gui_schema(date, start_city, end_city):
    """
    Check distinct IDs, route direction and the GUI Flight schema.

    @param date: Date string in the agreed two-digit-year format.
    @param start_city: Departure city to preserve.
    @param end_city: Arrival city to preserve.
    @return: None.
    """
    record = make_flight_record(21, 7, 13, date, start_city, end_city)

    assert record == {
        "Flight_ID": 21,
        "Client_ID": 7,
        "Airline_ID": 13,
        "Date": date,
        "Start City": start_city,
        "End City": end_city
    }


@pytest.mark.parametrize(
    "factory, arguments, field",
    [
        (
            make_client_record,
            (
                7, "Anna Kowalska", "12 High Street", "", "", "Luton",
                "Bedfordshire", "LU1 1XX", "UK", "07123456789"
            ),
            "Name"
        ),
        (make_airline_record, (13, "British Airways"), "Company Name"),
        (
            make_flight_record,
            (21, 7, 13, "26-09-18 14:30", "London", "Paris"),
            "Start City"
        )
    ]
)
def test_factories_return_independent_records(factory, arguments, field):
    """
    Check that changing one record does not affect another record.

    @param factory: Record creation function to check.
    @param arguments: Values supplied to both function calls.
    @param field: Text field to change in the first record.
    @return: None.
    """
    first = factory(*arguments)
    second = factory(*arguments)
    original_value = second[field]
    first[field] = "Changed value"

    assert first is not second
    assert second[field] == original_value
    assert factory(*arguments)[field] == original_value
