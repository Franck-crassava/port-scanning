import socket
import sys

def scan_ports(target_ip, ports):
    print(f"\n[+] Scanning {target_ip} on ports: {ports}\n")
    
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            else:
                print(f"[CLOSED] Port {port}")
            s.close()
        except Exception as e:
            print(f"[ERROR] Could not scan port {port} - {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python port_scanner.py <target_ip> <port1> <port2> ... <portN>")
        print("Example: python port_scanner.py 192.168.1.1 22 80 443")
        sys.exit(1)

    target_ip = sys.argv[1]
    try:
        ports = [int(port) for port in sys.argv[2:]]
    except ValueError:
        print("[!] Please provide only valid port numbers (integers).")
        sys.exit(1)

    scan_ports(target_ip, ports)

if __name__ == "__main__":
    main()
