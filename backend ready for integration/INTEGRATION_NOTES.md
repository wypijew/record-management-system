# Backend integration draft

This is a working copy based on the team's reviewed backend ZIP. The original files
were not overwritten. The backend has **not** yet been wired to Maram's GUI.

## Record contract

- Client: `ID`, `Type: "Client"` and the same named fields as the client form.
- Airline: `ID`, `Type: "Airline"`, `Company Name`.
- Flight: `Flight_ID`, `Client_ID`, `Airline_ID`, `Date`,
  `Start City`, `End City`.
- Dates use `YY-MM-DD HH:MM`, for example `26-09-18 14:30`.
- IDs must be positive integers and unique within a record type. A Client,
  Airline and Flight may each have the same numeric ID.

Client address lines 2 and 3 must be present as keys, but may contain empty
strings, matching Maram's form and the requirements checklist.

The Flight form's existing dictionary does not need a `Type` key. Backend
functions recognise Flight records by their `Flight_ID` key. Client and Airline
form dictionaries already include `Type`. All three GUI windows must use the same
`records` list loaded with
`load_records("records.json")`, rather than their separate temporary lists.
Connect GUI buttons to `create_record`, `search_records`, `update_record` and
`delete_record`, and save the shared list on application close. Search takes
`(records, record_id, record_type)`; update takes
`(records, record_id, changed_fields, record_type)`; delete takes
`(records, record_id, record_type)`. Creation and update return a boolean,
so the GUI should show success only when the call succeeds.

`main.py` remains a backend startup placeholder; it loads and immediately
saves records. Maram and DJ still need to connect startup/shutdown to the GUI.

Run `python -m pytest test_backend_integration.py` from this directory.
The older standalone validator tests were written for `ID` on Flight records;
they need updating for this agreed GUI-compatible format before being added to
the integrated test run.
