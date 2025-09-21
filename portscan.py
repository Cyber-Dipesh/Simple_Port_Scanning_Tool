#!/usr/bin/python
import socket
socket.setdefaulttimeout(2)
host = input("[*] Enter host/ip to scan: ")

def portscanner(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        else:
            print(f"[!!] Port {port} is closed")
        sock.close()
    except Exception as e:
        print(f"[!!] Error scanning port {port}: {e}")

print("[+] 1. For Single Port Scan " )
print("[+] 2. For 1k port Scan")

user = int(input())
if (user== 1):
	p = int(input("Enter port number : "))
	portscanner(p)
elif (user == 2):
	for port in range(1, 1000):
		portscanner(port)
else:
	print("INVALID INPUT")
