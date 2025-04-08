import socket
import argparse
import threading
from datetime import datetime

lock = threading.Lock()

def banner_grab(ip, port):
    try:
        with socket.socket() as s:
            s.settimeout(2)
            s.connect((ip, port))
            banner = s.recv(1024).decode().strip()
            return banner
    except:
        return "No banner"

def scan_port(ip, port, output_file=None):
    try:
        with socket.socket() as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                banner = banner_grab(ip, port)
                msg = f"[OPEN] Port {port} | Banner: {banner}"
            else:
                msg = f"[CLOSED] Port {port}"

            with lock:
                print(msg)
                if output_file:
                    with open(output_file, "a") as f:
                        f.write(msg + "\n")

    except Exception as e:
        print(f"[ERROR] Port {port}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Python Port Scanner Tool")

    parser.add_argument("ip", help="Target IP address")
    parser.add_argument("-p", "--ports", nargs="+", type=int, required=True, help="List of ports to scan")
    parser.add_argument("-o", "--output", help="Output file to save results")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads (default: 10)")

    args = parser.parse_args()

    print(f"\n🔎 Starting scan on {args.ip}")
    print(f"📅 Time: {datetime.now()}")
    print(f"🎯 Ports: {args.ports}")
    print(f"⚙️ Threads: {args.threads}")
    print("------------------------------\n")

    threads = []
    for port in args.ports:
        t = threading.Thread(target=scan_port, args=(args.ip, port, args.output))
        t.start()
        threads.append(t)

        # Limite les threads simultanés
        while threading.active_count() > args.threads:
            pass

    for t in threads:
        t.join()

    print("\n✅ Scan finished.")

if __name__ == "__main__":
    main()
