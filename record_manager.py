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
  return [record for record in records if record.get("Type) == record_type]

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
    if record.get("ID" == record_id:
      if record_type is not None and record.get("Type") != record_type:
        continue

      updated_record = record.copy()
      updated_record.update(updated_data)

      if not validate_record(updated_record, records, current_it=record_id):
        return False

      record.update(updated_data)
      return True

    return False

  
