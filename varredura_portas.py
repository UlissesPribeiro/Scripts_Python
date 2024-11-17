import socket
host = input("Digite o IP ou domínio: ")
port_start = int(input("Porta inicial: "))
port_end = int(input("Porta final: "))
for port in range(port_start, port_end + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    if not sock.connect_ex((host, port)):
        print(f"Porta {port} aberta.")
    sock.close()
