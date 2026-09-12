# storage.py
# load/save records from JSON L file
# supporting startup and shutdown

import json
import os

def load_records(filename):
  if os.path.exists(filename):
    with open(filename, "r") as file:
      return json.load(file)
  return []

def save_records(filename, records):
  with open(filename, "w") as file:
    json.dump(records, file, indent=3)
