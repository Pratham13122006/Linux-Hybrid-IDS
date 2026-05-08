# Project IDS

A lightweight Intrusion Detection System (IDS) project built using Python. The project is designed for learning cybersecurity concepts such as packet sniffing, login attack detection, SQL injection detection, fake attack simulation, and alert monitoring.

## Features

* Packet sniffing and network monitoring
* Nmap scan detection
* SQL injection detection
* Fake hacker attack simulation for testing
* Login monitoring system
* Dashboard frontend using HTML
* Alert logging system

---

# Project Structure

```bash
project ids/
│
├── detection/
│   ├── login_detector.py
│   └── sqli_detector.py
│
├── nids/
│   └── packet_sniffer.py
│
├── simulation/
│   └── fake_hacker.py
│
├── templates/
│   ├── index.html
│   └── login.html
│
├── events.py
├── main.py
└── README.md
```

---

# Technologies Used

* Python
* Flask
* Scapy
* HTML/CSS
* JavaScript

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

## 2. Open Project Folder

```bash
cd YOUR-REPOSITORY
```

## 3. Install Dependencies

```bash
pip install flask scapy
```

---

# Running the Project

Start the Flask server:

```bash
python main.py
```

Open your browser and visit:

```bash
http://127.0.0.1:5000
```

---

# Running Attack Simulations

## Fake Hacker Simulation

```bash
python simulation/fake_hacker.py
```

## Nmap Scan Test

Run from Kali Linux:

```bash
nmap -sS TARGET-IP
```

## Hydra Brute Force Test

```bash
hydra -l admin -P passwords.txt TARGET-IP http-post-form "/login:username=^USER^&password=^PASS^:Invalid"
```

---

# Alerts Detected

The IDS can currently detect:

* High-rate packet scans
* Suspicious login attempts
* SQL injection attempts
* Brute-force style activity

---

# Future Improvements

* Real-time dashboard updates
* Machine learning based detection
* Email alert notifications
* Database logging
* Advanced traffic analysis

---

# Author

Pratham Jain

---

# Disclaimer

This project is for educational and ethical cybersecurity learning purposes only. Do not use it against systems without proper authorization.
