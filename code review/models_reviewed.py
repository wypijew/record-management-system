"""
REVIEW: Please apply the University's "Coding Standard" consistently
throughout this file. Use 4 spaces per indentation level and keep code
lines within the recommended 79-character limit.

Please also use two blank lines between top-level function definitions.

Add appropriate comments/documentation before each self-contained block
of code to explain its purpose and intended logic.

Please also add docstrings to functions in accordance with the
University's Coding Standard. Docstrings should describe the function's
purpose, input parameters and return values.

Please refer to the "Coding Standard" document for the full formatting
and documentation guidance.
"""

# models.py for client, airline, and flight record

# REVIEW: This function definition exceeds the recommended 79-character
# line length. Split the parameters across multiple lines and use
# 4-space indentation in accordance with the Coding Standard.
def make_client_record(record_id, name, address1, address2, address3, city, state, zip_code, country, phone):
  return {
    "ID" : record_id,
    # REVIEW: Change "type" to "Type" to keep the key consistent with
    # validators.py and the other record types. Dictionary keys are
    # case-sensitive, so "type" and "Type" are treated as different keys.
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
    # REVIEW: Add a comma after this dictionary item. Without it, the
    # dictionary syntax is invalid and models.py cannot be imported.
    "ID": record_id
    "Type" : "Airline",
    # REVIEW: Replace "Airline Name" with "Company Name" to match the
    # assignment brief. Consider renaming airline_name to company_name as
    # well, so the parameter and dictionary field use consistent
    # terminology.
    "Airline Name" : airline_name
  }

# REVIEW: This function definition also exceeds the recommended
# 79-character line length. Split the parameters across multiple lines.
def make_flight_record(record_id, client_id, airline_id, date, departure_city, arrival_city):
  return {
    "ID": record_id,
    "Type": "Flight",
    # REVIEW: Add a comma after this dictionary item, as above.
    "Client_ID": client_id
    "Airline_ID": airline_id,
    "Date": date,
    # REVIEW: Replace "Departure" with "Start City" to match the
    # assignment brief. Consider renaming departure_city to start_city
    # as well.
    # REVIEW: Add a comma after this dictionary item.
    "Departure": departure_city
    # REVIEW: Replace "Arrival" with "End City" to match the assignment
    # brief. Consider renaming arrival_city to end_city as well.
    "Arrival": arrival_city
  }

