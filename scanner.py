
import socket

print("=" * 45)
print("        NETWORK PORT SCANNER")
print("=" * 45)

target = input("Enter IP address or hostname: ")

try:
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    if not (1 <= start_port <= end_port <= 65535):
        raise ValueError

except ValueError:
    print("Invalid port range.")
    exit()

try:
    target_ip = socket.gethostbyname(target)
    print(f"\nTarget IP: {target_ip}")

except socket.gaierror:
    print("Invalid hostname or IP address.")
    exit()

open_ports = 0
closed_ports = 0

print(f"\nScanning ports {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port, "tcp")
                except OSError:
                    service = "Unknown"

                print(f"Port {port:<6} OPEN       {service}")
                open_ports += 1
            else:
                closed_ports += 1

    except socket.error:
        print(f"Error checking port {port}")

print("\n" + "=" * 45)
print("             SCAN RESULTS")
print("=" * 45)
print(f"Open ports:   {open_ports}")
print(f"Other ports:  {closed_ports}")
print("Scan completed.")
