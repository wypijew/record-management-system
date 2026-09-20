# storage.py
# Load and save records using a JSON file.
# Support persistent storage between application sessions.

import json
import os


def load_records(filename):
    """
    Load records from a JSON file.

    @param filename: Path to the JSON file containing the records.
    @return: List of stored records, or an empty list if unavailable.
    """
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_records(filename, records):
    """
    Save records to a JSON file.

    @param filename: Path to the JSON file used for storage.
    @param records: List of records to save.
    @return: None.
    """
    with open(filename, "w") as file:
        json.dump(records, file, indent=3)