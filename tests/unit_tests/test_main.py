"""Unit tests for the backend application entry point."""

import json
import runpy

import main


def test_main_loads_records_and_saves_the_same_list(monkeypatch):
    """
    Check that main saves the records returned by persistent storage.

    @param monkeypatch: Pytest fixture used to replace storage functions.
    @return: None.
    """
    records = [{"ID": 1, "Type": "Airline", "Company Name": "Air"}]
    calls = []

    def fake_load_records(filename):
        """
        Record the load call and return prepared records.

        @param filename: Filename supplied by main.
        @return: Prepared record list.
        """
        calls.append(("load", filename))
        return records

    def fake_save_records(filename, saved_records):
        """
        Record the save call and its record list.

        @param filename: Filename supplied by main.
        @param saved_records: Records supplied by main.
        @return: None.
        """
        calls.append(("save", filename, saved_records))

    monkeypatch.setattr(main, "load_records", fake_load_records)
    monkeypatch.setattr(main, "save_records", fake_save_records)

    main.main()

    assert calls == [
        ("load", "records.json"),
        ("save", "records.json", records)
    ]


def test_running_main_file_creates_an_empty_json_file(tmp_path, monkeypatch):
    """
    Check that running main as a script creates its storage file.

    @param tmp_path: Temporary path fixture supplied by pytest.
    @param monkeypatch: Pytest fixture used to change the working directory.
    @return: None.
    """
    monkeypatch.chdir(tmp_path)

    runpy.run_path(main.__file__, run_name="__main__")

    filename = tmp_path / "records.json"
    assert filename.exists()
    assert json.loads(filename.read_text()) == []