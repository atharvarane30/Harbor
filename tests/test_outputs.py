import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), "report.json was not created"

    try:
        with REPORT_PATH.open() as f:
            return json.load(f)
    except json.JSONDecodeError as exc:
        raise AssertionError("report.json is not valid JSON") from exc


def test_report_has_expected_content():
    report = load_report()

    assert report == {
        "total_requests": 6,
        "unique_ips": 3,
        "top_path": "/index.html",
    }
