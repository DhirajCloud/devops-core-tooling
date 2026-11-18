"""Dashboard utilities for DevOps Core Tooling."""


def get_dashboard_summary():
    """Return a summary of the DevOps project."""
    return {
        "project": "DevOps Core Tooling",
        "environment": "development",
        "modules": ["authentication", "logging"],
        "status": "active",
    }


def display_dashboard():
    """Display the project dashboard."""
    summary = get_dashboard_summary()

    print("===== DEVOPS PROJECT DASHBOARD =====")
    print(f"Project: {summary['project']}")
    print(f"Environment: {summary['environment']}")
    print(f"Modules: {', '.join(summary['modules'])}")
    print(f"Status: {summary['status']}")


if __name__ == "__main__":
    display_dashboard()
