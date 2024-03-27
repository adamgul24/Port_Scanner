import socket

def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        return True
    except:
        return False

def main():
    target_ip = input("Enter the IP address to scan: ")
    for port in range(1, 1025):
        if scan_port(target_ip, port):
            print(f"Port {port} is open on {target_ip}")

if __name__ == "__main__":
    main()
