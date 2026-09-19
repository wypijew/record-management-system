"""Unit tests for JSON record storage."""

import json

from storage import load_records, save_records


def test_load_records_returns_empty_list_when_file_is_missing(tmp_path):
    """
    Check that loading a missing file returns an empty list.

    @param tmp_path: Temporary path fixture supplied by pytest.
    @return: None.
    """
    filename = tmp_path / "missing_records.json"

    assert load_records(filename) == []


def test_load_records_returns_empty_list_for_invalid_json(tmp_path):
    """
    Check that loading invalid JSON returns an empty list.

    @param tmp_path: Temporary path fixture supplied by pytest.
    @return: None.
    """
    filename = tmp_path / "invalid_records.json"
    filename.write_text("not valid JSON")

    assert load_records(filename) == []


def test_load_records_returns_data_from_a_valid_json_file(tmp_path):
    """
    Check that existing JSON data is returned unchanged.

    @param tmp_path: Temporary path fixture supplied by pytest.
    @return: None.
    """
    filename = tmp_path / "stored_records.json"
    expected_records = [
        {"ID": 1, "Type": "Airline", "Company Name": "London Air"}
    ]
    filename.write_text(json.dumps(expected_records))

    assert load_records(filename) == expected_records


def test_save_records_writes_data_that_can_be_loaded(tmp_path):
    """
    Check that saved records can be loaded with their text unchanged.

    @param tmp_path: Temporary path fixture supplied by pytest.
    @return: None.
    """
    filename = tmp_path / "records.json"
    records = [
        {
            "ID": 1,
            "Type": "Client",
            "Name": "Lucas Green",
            "City": "London"
        }
    ]

    save_records(filename, records)

    assert filename.exists()
    assert load_records(filename) == records


def test_save_records_overwrites_existing_file_contents(tmp_path):
    """
    Check that saving replaces existing JSON data in the target file.

    @param tmp_path: Temporary path fixture supplied by pytest.
    @return: None.
    """
    filename = tmp_path / "records.json"
    previous_records = [{"ID": 1, "Type": "Airline", "Company Name": "Old"}]
    new_records = [{"ID": 2, "Type": "Airline", "Company Name": "New"}]
    filename.write_text(json.dumps(previous_records))

    save_records(filename, new_records)

    assert load_records(filename) == new_records