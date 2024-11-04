import socket

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Tempo limite de 1 segundo
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

ip_address = input("Digite o endereço IP para escanear: ")
ports_to_scan = [21, 22, 23, 25, 80, 443]  # Exemplos de portas comuns

for port in ports_to_scan:
    if scan_port(ip_address, port):
        print(f"Porta {port} está aberta em {ip_address}.")
    else:
        print(f"Porta {port} está fechada em {ip_address}.")
