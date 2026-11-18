from dashboard import get_dashboard_summary


def test_dashboard_summary():
    summary = get_dashboard_summary()

    assert summary["project"] == "DevOps Core Tooling"
    assert summary["environment"] == "development"
    assert "authentication" in summary["modules"]
    assert "logging" in summary["modules"]
    assert summary["status"] == "active"
