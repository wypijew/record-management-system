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
# storage.py

# REVIEW: The implementation uses standard JSON rather than JSONL.
# json.load() reads a complete JSON document and json.dump() writes
# the records list as a complete JSON document. Update this comment
# so that it accurately describes the storage format used.
# If JSON is retained as the storage format, please also update
# requirements.txt, as the jsonlines dependency is no longer required.
# load/save records from JSON L file
# supporting startup and shutdown

import json
import os


def load_records(filename):
  # REVIEW: Consider handling an existing empty or invalid JSON file.
  # json.load() raises JSONDecodeError if the file exists but does not
  # contain valid JSON, which could prevent the application from starting.
  if os.path.exists(filename):
    with open(filename, "r") as file:
      return json.load(file)
  return []

def save_records(filename, records):
  with open(filename, "w") as file:
    json.dump(records, file, indent=3)
