from scapy.all import sniff, IP, TCP

def process_packet(packet):
    """
    This callback function triggers every time a packet passes the filter.
    """
    # check if the packet has an IP layer (network layer)
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        # check if the packet jas a TCP layer (transport layer)
        if packet.haslayer(TCP):
            sport = packet[TCP].sport
            dport = packet[TCP].dport

            print(f"[+] Packet: {ip_src}:{sport} -> {ip_dst}:{dport}")

            # if there is raw data/text payload in the http packet, display it
            if packet[TCP].payload:
                raw_data = str(packet[TCP]. payload)
                # clean up output for basic terminal reading
                clean_preview = raw_data[:100] # show first 100 characters
                print(f"     Payload Preview: {clean_preview}\n")

def main():
    print("[*] Starting Python Network Sniffer...")
    print("[*] Filtering for unencrypted HTTP traffic *(Port 80)...")
    print("[*] Press Ctrl+C to stop.")

    # BPF filter 'tcp port 80' isolates only unencrypted web traffic
    # store=0 tells scapy to discard packets after processing them memory bloat 
    sniff(filter="tcp port 80", prn=process_packet, store=0)

if __name__ == "__main__":
    main()