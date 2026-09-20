

"""Tests for the application entry point."""

import runpy

import main


def test_main_starts_gui(monkeypatch):
    """Check that main starts the GUI application."""
    calls = []

    def fake_run_app():
        """Record that the GUI start function was called."""
        calls.append("run_app")

    monkeypatch.setattr(main, "run_app", fake_run_app)

    main.main()

    assert calls == ["run_app"]


def test_running_main_file_starts_gui(monkeypatch):
    """Check that running main.py executes the GUI start function."""
    calls = []

    def fake_run_app():
        """Record that the GUI start function was called."""
        calls.append("run_app")

    monkeypatch.setattr("src.gui.app.run_app", fake_run_app)

    runpy.run_path(main.__file__, run_name="__main__")

    assert calls == ["run_app"]