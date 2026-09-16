# storage.py
# load/save records from JSON L file
# supporting startup and shutdown

# REVIEW: This issue remains from the previous review. The implementation
# uses standard JSON rather than JSONL. Please update this comment so that
# it accurately describes the storage format currently used.
# If JSON is retained, please also remove the unnecessary jsonlines
# dependency from requirements.txt.

# REVIEW: The Coding Standard points from the previous review still need
# to be applied to this file. Please use 4 spaces per indentation level,
# add appropriate type hints and docstrings, and use two blank lines
# between top-level function definitions.

import json
import os

def load_records(filename):

  # REVIEW: This issue remains from the previous review. Please handle an
  # existing empty or invalid JSON file. json.load() raises JSONDecodeError
  # if the file does not contain valid JSON, which could prevent the
  # application from starting. For example, this can be handled using:
  #
  # try:
  #     with open(filename, "r") as file:
  #         return json.load(file)
  # except json.JSONDecodeError:
  #     return []
  if os.path.exists(filename):
    with open(filename, "r") as file:
      return json.load(file)
  return []

def save_records(filename, records):
  with open(filename, "w") as file:
    json.dump(records, file, indent=3)


# REVIEW SUMMARY:
# The main functional structure of the storage module remains simple and
# appropriate for loading and saving the records using standard JSON.
#
# However, several points identified in the previous review still need to
# be addressed. These mainly concern consistency between the documented
# storage format and the implementation, application of the University's
# Coding Standard, and handling an existing empty or invalid JSON file.
#
# Thank you for reviewing these points.
#
# Remaining REVIEW comments can be found at:
# - Lines 5-9: JSON/JSONL consistency and the jsonlines dependency.
# - Lines 11-14: application of the University's Coding Standard.
# - Lines 21-30: handling an empty or invalid JSON file.
#
# Please check all REVIEW comments before the final version is integrated.