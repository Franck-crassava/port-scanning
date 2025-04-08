# 🔎 scanning-port

A lightweight and customizable Python-based port scanner designed for learning, pentesting practice, and automation.  
Easily specify target IPs, ports, output options, and scan multiple ports in parallel using threads.

---

## ⚙️ Features

- 🔧 CLI-based configuration (target IP, ports, thread count)
- 🧵 Multithreaded scanning for speed
- 📄 Output results to a file
- 🎯 Banner grabbing from open ports (optional)
- 🔒 Simple and clean Python code, beginner-friendly
- 🚀 Fast and effective for quick reconnaissance

---

## 🛠️ Usage

```bash
python port_scanner.py <target_ip> -p <port1> <port2> ... -o <output_file> -t <threads>
```
✅ Example
```bash
python port_scanner.py 192.168.1.1 -p 22 80 443 8080 -o scan_results.txt -t 20
```
## 📥 Arguments
Argument	Description	Required	Example
<target_ip>	IP address of the target	✅	192.168.1.1
-p	List of ports to scan	✅	-p 22 80 443
-o	Output file to save results	❌	-o results.txt
-t	Number of threads (default: 10)	❌	-t 20

## 📌 Notes
Banner grabbing is attempted on open ports only.

If no output file is specified, results are printed to the console.

The script uses threading to enhance scan speed, especially on larger port lists.

## 🧠 Learn More
This project is part of a personal portfolio to explore cybersecurity tooling.
More tools and scripts coming soon!

## 📂 Folder Structure
```bash
.
├── port_scanner.py   # Main script
├── README.md         # Documentation
└── results.txt       # Output file (if specified)
```

## 📅 Created: 2025

## 💼 Status: Work-in-progress

## 📝 License
MIT License – Free to use and modify.

## 🧑‍💻 Author
Franck CRASSAVA – Cybersecurity & Network Architecture Student

## ⚠️ Disclaimer
This tool is intended for educational purposes only.
Do not scan systems you don't own or have explicit permission to test.
