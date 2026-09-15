"""
Models Module

Provides factory functions to create client, airline, and flight records.
Each function returns a dictionary representing the record with the required fields.

This block of code has been proofread by Copilot using the same University coding standard for PEP-8,
identifier names, Pydoc docstrings and comments before code.
Below is the prompt that I used
Apply the same coding standard as other blocks that I've given you and 
proofread for typos or any syntax error issues.
"""


def make_client_record(record_id: int, name: str, address1: str, address2: str,
                       address3: str, city: str, state: str, zip_code: str,
                       country: str, phone: str) -> dict:
    """
    Creates a client record.

    @param record_id: Unique integer ID for the client
    @param name: Client's full name
    @param address1: Primary address line
    @param address2: Secondary address line
    @param address3: Tertiary address line
    @param city: City of residence
    @param state: State of residence
    @param zip_code: Postal code
    @param country: Country of residence
    @param phone: Phone number
    @return: Dictionary representing the client record
    """
    return {
        "ID": record_id,
        "Type": "Client",  # 🔧 FIXED: corrected "type" → "Type"
        "Name": name,
        "Address Line 1": address1,
        "Address Line 2": address2,
        "Address Line 3": address3,
        "City": city,
        "State": state,
        "Zip Code": zip_code,
        "Country": country,
        "Phone Number": phone
    }


def make_airline_record(record_id: int, airline_name: str) -> dict:
    """
    Creates an airline record.

    @param record_id: Unique integer ID for the airline
    @param airline_name: Name of the airline
    @return: Dictionary representing the airline record
    """
    return {
        "ID": record_id,  # 🔧 FIXED: added missing comma
        "Type": "Airline",
        "Airline Name": airline_name
    }


def make_flight_record(record_id: int, client_id: int, airline_id: int,
                       date: str, departure_city: str, arrival_city: str) -> dict:
    """
    Creates a flight record.

    @param record_id: Unique integer ID for the flight
    @param client_id: ID of the client associated with the flight
    @param airline_id: ID of the airline associated with the flight
    @param date: Date and time of the flight (string format)
    @param departure_city: Departure city
    @param arrival_city: Arrival city
    @return: Dictionary representing the flight record
    """
    return {
        "ID": record_id,
        "Type": "Flight",
        "Client_ID": client_id,  # 🔧 FIXED: added missing comma
        "Airline_ID": airline_id,
        "Date": date,
        "Departure": departure_city,  # 🔧 FIXED: added missing comma
        "Arrival": arrival_city
    }
