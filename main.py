from flask import Flask, render_template, request, redirect, session
from threading import Thread

from events import get_alerts
from nids.packet_sniffer import start_sniffer

app = Flask(__name__)

# Secret key for sessions
app.secret_key = "hybrid_ids_secret_key"

# Demo credentials
USERNAME = "admin"
PASSWORD = "admin123"


# ---------------- LOGIN PAGE ----------------

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():

    # If already logged in
    if session.get("logged_in") is True:
        return redirect("/dashboard")

    if request.method == "POST":

        username = request.form.get("username", "")
        password = request.form.get("password", "")

        # SQL Injection Detection
        sql_patterns = [
            "' OR",
            "1=1",
            "--",
            "UNION",
            "SELECT"
        ]

        for pattern in sql_patterns:

            if (
                pattern.lower() in username.lower()
                or pattern.lower() in password.lower()
            ):

                return render_template(
                    "login.html",
                    error="SQL Injection Attempt Detected!"
                )

        # Normal Login
        if username == USERNAME and password == PASSWORD:

            session["logged_in"] = True

            return redirect("/dashboard")

        else:

            return render_template(
                "login.html",
                error="Invalid username or password"
            )

    return render_template("login.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    logged_in = session.get("logged_in", False)

    if logged_in is not True:
        return redirect("/login")

    alerts = get_alerts()

    return render_template(
        "index.html",
        alerts=alerts
    )


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


# ---------------- START NIDS ----------------

def run_nids():
    start_sniffer()


if __name__ == "__main__":

    print("[+] Starting Hybrid IDS System...")

    # Start NIDS thread
    sniffer_thread = Thread(target=run_nids)
    sniffer_thread.daemon = True
    sniffer_thread.start()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
        use_reloader=False
    )