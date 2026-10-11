import socket

def dns_lookup(domain):
    try:
        print(f"\nLooking up: {domain}\n")

        ip = socket.gethostbyname(domain)
        print(f"IP Address: {ip}")

        try:
            hostname, aliaslist, ipaddrlist = socket.gethostbyaddr(ip)
            print(f"Hostname: {hostname}")
        except socket.herror:
            print("Hostname: Not available")

    except socket.gaierror:
        print("Error: Inavalid domain or network issue")

while True:
    domain = input("\nEnter domain (or type 'exit'): ")

    if domain.lower() == "exit":
        break

    dns_lookup(domain)
    