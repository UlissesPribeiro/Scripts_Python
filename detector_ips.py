from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp = ARP(pdst=ip_range)
    packet = ether / arp
    result = srp(packet, timeout=2, verbose=False)[0]
    
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

ip_range = input("Digite o intervalo de IP para escanear (ex: 192.168.1.1/24): ")
devices = scan_network(ip_range)

print("Dispositivos encontrados na rede:")
for device in devices:
    print(f"IP: {device['ip']}, MAC: {device['mac']}")
