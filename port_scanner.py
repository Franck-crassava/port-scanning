import socket

target = input("Enter IP to scan: ")
ports = [22, 80, 443, 3389, 8080]

print(f"Scanning {target}...\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    s.close()
