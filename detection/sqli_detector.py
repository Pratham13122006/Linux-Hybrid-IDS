import re
import time
import urllib.parse
from events import add_alert

patterns = [
    r"(\%27)|(\')|(\-\-)|(\%23)|(#)",
    r"\b(OR|AND)\b.+=",
    r"UNION",
]

def detect_sqli(event):
    raw_payload = event.get("payload", "")
    ip = event.get("ip")

    # Decode URL encoding (fix for %20 etc.)
    payload = urllib.parse.unquote(raw_payload)

    for pattern in patterns:
        if re.search(pattern, payload, re.IGNORECASE):
            add_alert({
                "type": "SQL Injection",
                "ip": ip,
                "time": time.strftime("%H:%M:%S"),
                "severity": "High",
                "message": f"Detected SQLi payload: {payload}"
            })
            break