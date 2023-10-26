from scapy.all import *

target_ip = "blueserver"  
target_port = 80

packet_data = "This is the packet data we intercepted and are re-sending."

def send_packet(packet_content):
    packet = IP(dst=target_ip)/TCP(dport=target_port, flags='S')/Raw(load=packet_content)
    
    response = sr1(packet, timeout=2)
    if response:
        print("Received response from target.")
    else:
        print("No response from target.")

def main():
    print(f"Sending intercepted packet data to {target_ip}:{target_port}")
    try:
        send_packet(packet_data)
        print("Packet sent.")
    except Exception as e:
        print(f"Error sending packet: {e}")

if __name__ == "__main__":
    main()
