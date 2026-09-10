# models.py for client, airline, and flight record

def make_client_record(record_id, name, address1, address2, address3, city, state, zip_code, country, phone):
  return {
    "ID" : record_id,
    "type" : "Client",
    "Name" : name,
    "Address Line 1" : address1,
    "Address Line 2" : address2,
    "Address Line 3" : address3,
    "City" : city,
    "State": state,
    "Zip Code" : zip_code,
    "Country" : country,
    "Phone Number": phone
  }

def make_airline_record(record_id, airline_name):
  return {
    "ID": record_id
    "Type" : "Airline",
    "Airline Name" : airline_name
  }

def make_flight_record(record_id, client_id, airline_id, date, departure_city, arrival_city):
  return {
    "ID": record_id,
    "Type": "Flight",
    "Client_ID": client_id
    "Airline_ID": airline_id,
    "Date": date,
    "Departure": departure_city
    "Arrival": arrival_city
  }
  
