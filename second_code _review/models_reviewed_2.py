"""
Models Module

Provides factory functions to create client, airline, and flight records.
Each function returns a dictionary representing the record with the required fields.

!REVIEW: Keep the module docstring focused on the purpose and functionality of the
module. The Copilot proofreading note and prompt describe the development process
rather than the module itself, so they should be removed from the final code and any
required GenAI use should be documented in the appropriate disclosure location. - in
the final report.!

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
        "Type": "Client",
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
        "ID": record_id,  #
        "Type": "Airline",
        #REVIEW: Please change Airline Name to Company Name to match the Airline record
        #structure specified in the assignment brief. For consistency, please also rename the
        #airline_name parameter to company_name and update the corresponding docstring.
        "Airline Name": airline_name
    }



# REVIEW: Replace "Departure" and "Arrival" with "Start City" and
# "End City" to match the Flight record structure specified in the
# assignment brief. For consistency, also rename departure_city and
# arrival_city to start_city and end_city and update the docstring.
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
        "Client_ID": client_id,
        "Airline_ID": airline_id,
        "Date": date,
        "Departure": departure_city,
        "Arrival": arrival_city
    }


# REVIEW SUMMARY:
# The latest revision addresses several issues identified in the previous
# review. In particular, the missing commas in the Airline and Flight
# dictionaries have been corrected, "type" has been changed to "Type" in
# the Client record, long function definitions have been reformatted, and
# type hints, docstrings, consistent indentation, and spacing between
# top-level functions have been added.
#
# The issues previously identified in the Client record have now been
# addressed, and no further changes are currently required in
# make_client_record().
#
# Thank you for addressing these points.
#
# Remaining REVIEW comments can be found at:
# - Lines 7-11: module documentation and the Copilot proofreading note.
# - Lines 65-67: Airline record structure and terminology.
# - Lines 73-76: Flight record structure and terminology.
#
# Please check all REVIEW comments before the final version is integrated.