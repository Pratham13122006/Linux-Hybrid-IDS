alerts = []

def add_alert(alert):
    # Add newest alert at top
    alerts.insert(0, alert)
    print(f"[ALERT ADDED] {alert}")

def get_alerts():
    return alerts