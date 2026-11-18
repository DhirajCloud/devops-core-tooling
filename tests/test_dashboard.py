from dashboard import get_dashboard_summary


def test_dashboard_summary():
    summary = get_dashboard_summary()

    assert summary["project"] == "DevOps Core Tooling"
    assert summary["environment"] == "development"
    assert "authentication" in summary["modules"]
    assert "logging" in summary["modules"]
    assert summary["status"] == "active"


def test_dashboard_data_validation():
    summary = get_dashboard_summary()

    assert isinstance(summary["modules"], list)
    assert len(summary["modules"]) > 0
    assert isinstance(summary["status"], str)
    assert summary["status"].strip() != ""
