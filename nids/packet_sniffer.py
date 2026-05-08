from scapy.all import sniff
from events import add_alert
import time

packet_tracker = {}

PACKET_THRESHOLD = 30
TIME_WINDOW = 5


def process_packet(packet):

    try:
        if packet.haslayer("IP"):

            src_ip = packet["IP"].src

            # Ignore localhost
            if src_ip == "127.0.0.1":
                return

            current_time = time.time()

            print(f"[PACKET] From {src_ip}")

            if src_ip not in packet_tracker:
                packet_tracker[src_ip] = []

            packet_tracker[src_ip].append(current_time)

            # Keep recent packets only
            packet_tracker[src_ip] = [
                t for t in packet_tracker[src_ip]
                if current_time - t < TIME_WINDOW
            ]

            packet_count = len(packet_tracker[src_ip])

            print(f"[TRACKING] {src_ip} -> {packet_count} packets")

            # Detect rapid packet flood / scan
            if packet_count >= PACKET_THRESHOLD:

                alert = {
                    "type": "Nmap Scan",
                    "ip": src_ip,
                    "time": time.strftime("%H:%M:%S"),
                    "severity": "High",
                    "message": f"Suspicious high-rate scan traffic detected ({packet_count} packets)"
                }

                add_alert(alert)

                print(f"[ALERT] Nmap Scan detected from {src_ip}")

                # Reset
                packet_tracker[src_ip] = []

    except Exception as e:
        print("[ERROR]", e)


def start_sniffer():

    print("[+] NIDS started (packet sniffing)...")

    sniff(
        store=0,
        prn=process_packet
    )