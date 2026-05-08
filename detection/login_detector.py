import time
from events import add_alert

login_attempts = {}
alerted_ips = {}

THRESHOLD = 5
WINDOW = 60
COOLDOWN = 60

def detect_login_abuse(event):
    if event.get("type") != "login":
        return

    ip = event.get("ip")
    success = event.get("success")

    if not ip:
        return

    now = time.time()

    # ✅ FIX: If login is successful → RESET and EXIT immediately
    if success:
        login_attempts[ip] = []
        alerted_ips[ip] = 0   # reset cooldown too
        return

    login_attempts.setdefault(ip, [])
    login_attempts[ip] = [t for t in login_attempts[ip] if now - t < WINDOW]
    login_attempts[ip].append(now)

    last_alert = alerted_ips.get(ip, 0)

    if len(login_attempts[ip]) >= THRESHOLD and (now - last_alert > COOLDOWN):
        alerted_ips[ip] = now

        add_alert({
            "type": "Login Abuse",
            "ip": ip,
            "time": time.strftime("%H:%M:%S"),
            "severity": "High",
            "message": f"{len(login_attempts[ip])} failed login attempts"
        })