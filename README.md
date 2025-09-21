# Simple_Port_Scanning_Tool
This script is a lightweight TCP port scanner built using Python's socket module. It allows users to check the status of individual ports or scan a range of ports (default: 1–999) on a target host/IP address. Designed for educational and diagnostic purposes, it demonstrates basic socket programming and network connectivity checks.

🚀 Features
- Scans a single port or a range of ports on a given host
- Uses connect_ex() for non-blocking connection attempts
- Timeout configurable via socket.setdefaulttimeout()
- Clean output indicating open/closed ports
- Exception handling for graceful error reporting

📦 Requirements
- Python 3.x
- No external dependencies

⚠️ Disclaimer
This tool is intended for educational use and authorized network diagnostics only. Do not scan hosts without explicit permission.
