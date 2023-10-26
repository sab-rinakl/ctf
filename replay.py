from scapy.all import *

target_ip = "blueserver"
target_port = 80
intercepted_packet = None

def packet_callback(packet):
    global intercepted_packet
    intercepted_packet = packet

def send_intercepted_packet(times=1):
    if intercepted_packet:
        intercepted_packet[IP].dst = target_ip
        intercepted_packet[TCP].dport = target_port
        for _ in range(times):
            send(intercepted_packet)
            print(f"Sent packet {(_ + 1)} to {target_ip}:{target_port}")
    else:
        print("No intercepted packet available to send.")

def main():
    try:
        sniff(filter="tcp", prn=packet_callback, count=1)
        send_intercepted_packet(times=5) 
    except KeyboardInterrupt:
        print("\nProcess stopped.")

if __name__ == "__main__":
    main()
