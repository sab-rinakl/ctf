from scapy.all import *

# IP of the target
target_ip = "192.168.1.3"  # Please replace this with the actual target IP
# Target port
target_port = 80

# Dummy packet data that we're 'replaying'
packet_data = "This is the packet data we intercepted and are re-sending."

def send_packet(packet_content):
    # Craft the packet with Scapy
    packet = IP(dst=target_ip)/TCP(dport=target_port)/Raw(load=packet_content)
    # Send the packet
    send(packet)

def main():
    print(f"Sending intercepted packet data to {target_ip}:{target_port}")
    send_packet(packet_data)
    print("Packet sent.")

if __name__ == "__main__":
    main()
