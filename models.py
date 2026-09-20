# models.py for Client, Airline, and Flight records


def make_client_record(
    record_id: int,
    name: str,
    address1: str,
    address2: str,
    address3: str,
    city: str,
    state: str,
    zip_code: str,
    country: str,
    phone: str
) -> dict:
    """
    Create and return a Client record.

    @param record_id: Unique identifier for the Client record.
    @param name: Client's name.
    @param address1: First line of the Client's address.
    @param address2: Second line of the Client's address.
    @param address3: Third line of the Client's address.
    @param city: Client's city.
    @param state: Client's state.
    @param zip_code: Client's zip code.
    @param country: Client's country.
    @param phone: Client's phone number.
    @return: Dictionary containing the Client record.
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


def make_airline_record(
    record_id: int,
    company_name: str
) -> dict:
    """
    Create and return an Airline record.

    @param record_id: Unique identifier for the Airline record.
    @param company_name: Name of the airline company.
    @return: Dictionary containing the Airline record.
    """
    return {
        "ID": record_id,
        "Type": "Airline",
        "Company Name": company_name
    }


def make_flight_record(
    record_id: int,
    client_id: int,
    airline_id: int,
    date: str,
    start_city: str,
    end_city: str
) -> dict:
    """
    Create and return a Flight record.

    @param record_id: Unique identifier for the Flight record.
    @param client_id: ID of the Client associated with the Flight.
    @param airline_id: ID of the Airline associated with the Flight.
    @param date: Flight date and time in YY-MM-DD HH:MM format.
    @param start_city: City where the Flight starts.
    @param end_city: City where the Flight ends.
    @return: Dictionary containing the Flight record.
    """
    return {
        "Flight_ID": record_id,
        "Client_ID": client_id,
        "Airline_ID": airline_id,
        "Date": date,
        "Start City": start_city,
        "End City": end_city
    }
