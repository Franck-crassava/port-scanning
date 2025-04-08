# 🔍 Port Scanner

A simple and lightweight Python script that scans a list of common ports on a given IP address. Useful for basic reconnaissance tasks or for learning how socket programming works in Python.

---

## 🚀 Features

- Scans multiple predefined ports
- Quick and easy to use
- Lightweight and beginner-friendly
- Customizable and easy to extend

---

## 🛠️ Requirements

- Python 3.x  
No external libraries are required — only the built-in `socket` module is used.

---

## 📦 Installation

```bash
git clone https://github.com/your-username/scanning-port.git
cd scanning-port
python port_scanner.py
```

🧠 How It Works
The script uses Python's built-in socket module to attempt TCP connections on a list of ports. If the connection is successful, the port is considered open.

📝 Usage
bash
Copier
Modifier
$ python port_scanner.py
Enter IP to scan: 192.168.1.1
Scanning 192.168.1.1...

Port 22 is closed
Port 80 is open
Port 443 is open
Port 3389 is closed
Port 8080 is closed
💡 By default, it scans: 22, 80, 443, 3389, 8080

🧑‍💻 Author
Franck CRASSAVA – Cybersecurity & Network Architecture Student

⚠️ Disclaimer
This tool is intended for educational purposes only.
Do not scan systems you don't own or have explicit permission to test.
