import socket
from unittest import result

# important ports and their services
ports = {
    21: ("FTP","Risk: Anonymous login may be enabled"),
    22: ("SSH", "Secure remote access"),
    23: ("Telnet", "High Risk: Unencrypted"),
    25: ("SMTP", "Check for mail abuse"),
    53: ("DNS", "DNS service"),
    80: ("HTTP", "Web Server"),
    443: ("HTTPS", "Secure Web Server"),
    3306: ("MySQL", "Database Exposed"),
    3389: ("RDP", "High Risk Remote Deskstop"),
    5432: ("PostgreSQL", "Database exposed"),
    8080: ("HTTP-Alt", "Alternative Web Server")
}

target = input("Enter target IP or hostname: ")

print(f"\nScanning {target}...\n")

open_found = False

for port, service in ports.items():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] {port} - {service}")
            open_found = True
        else:
            print(f"[closed] {port} - {service}")    

        sock.close()

    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        
if not open_found:
    print("\nNo open ports found in this scan lists.")

print("\nScan complete.")            