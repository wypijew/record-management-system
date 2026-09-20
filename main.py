# main.py
# Application entry point for the Record Management System.

from storage import load_records, save_records


FILENAME = "records.json"


def main():
    """
    Load existing records and prepare the application for GUI integration.

    @return: None.
    """
    # Load existing records from persistent storage when the application
    # starts.
    records = load_records(FILENAME)

    # GUI integration will use the loaded records here.

    # Save the current records to persistent storage before the
    # application closes.
    save_records(FILENAME, records)


if __name__ == "__main__":
    main()


# Final version notes:
# Removed temporary sample data and backend test operations because they
# should not run whenever the application starts.
# Removed imports that were only required by the temporary test code.
# The application now loads existing records at startup and saves them
# before closing.
# Final integration and save-on-close behaviour will be completed once
# the GUI implementation is available.