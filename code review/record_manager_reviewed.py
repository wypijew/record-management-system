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

# record_manager.py
# creating, finding, getting, creating, deleting, updating record

from validators import validate_record

def id_exists(records, record_id):
  for record in records:
    if record.get("ID") == record_id:
      return True
  return False

def find_record_by_id(records, record_id):
  for record in records:
    if record.get("ID") == record_id:
      return record
  return None

def get_records_by_type(records, record_type):
  # REVIEW: Add the missing closing quotation mark after "Type".
  # Without it, the string is unterminated and causes a syntax error,
  # preventing record_manager.py from being imported.
  # REVIEW: This line also exceeds the recommended 79-character limit.
  # Split the list comprehension across multiple lines.
  return [record for record in records if record.get("Type) == record_type]

# REVIEW: Replace "==" with "=" when assigning the default value to
# record_type. Function parameters use "=" for default values, whereas
# "==" is a comparison operator. The current syntax prevents the module
# from being imported.
def search_records(records, record_id=None, record_type==None):
  results = []

  for record in records:
    if record_id is not None and record.get("ID") != record_id:
      continue
    if record_type is not None and record.get("Type") != record_type:
      continue
    results.append(record)

  return results

def create_record(records, new_record):
  if not validate_record(new_record, records):
    return False

  # REVIEW: Replace the comma with a dot to call the append() method
  # on the records list. The current statement does not add the new
  # record to the list.
  records,append(new_record)
  return True

def delete_record(records, record_id, record_type=None):
  for record in records:
    if record.get("ID") == record_id:
      if record_type is None or record.get("Type") == record_type:
        records.remove(record)
        return True
  return False

def update_record(records, record_id, updated_data, record_type=None):
  for record in records:
    # REVIEW: Close the record.get() call after "ID" before comparing its
    # value with record_id. The current expression contains invalid syntax
    # and prevents record_manager.py from being imported.
    if record.get("ID" == record_id:
      if record_type is not None and record.get("Type") != record_type:
        continue

      updated_record = record.copy()
      updated_record.update(updated_data)

      # REVIEW: Replace "current_it" with "current_id" to match the parameter
      # expected by validate_record(). The current keyword argument name does
      # not correspond to the validator's function signature.
      if not validate_record(updated_record, records, current_it=record_id):
        return False

      record.update(updated_data)
      return True

    # REVIEW: Move this return statement outside the for loop. In its
    # current position, the function can return False after checking only
    # the first record instead of searching the complete records list.
    return False


