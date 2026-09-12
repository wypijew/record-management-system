# this is how the backend pieces will connect
# can use for initial testing before GUI is built


#main.py

from models import make_client_record, make_airline_record, make_flight_record
from record_manager import create_record, search_records, update_record, delete_record
from storage import load_records, save_records

FILENAME = "records.json"


def main():
  records = load_records(FILENAME)

  # Sample data creation
  client = make_client_record(
    1, "James Kim", "1 Main Street", "", "", "Newyork", "Newyork", "10977", "US" "12345678"
  )

  airline = make_airline_record(2, "American Airline"
                               )

  create_record(records, client)
  create_record(records, airline)
  create_record(records, flight)

  print("All records:")
  print(records)

  print("\nSearch ID 1:")
  print(search_records(records, record_id=1))

  update_record(records, 1, {"City": "Boston"}. record_type="Client")

  print("\nAfter update:")
  print(search_records(records, record_id=1))

  delete_record(records, 3, record_type="Flight")

  print("\nAfter deleting flight:")
  print(records)

  save_records(FILENAME, records)

if __name__ == "__main__":
  main()
