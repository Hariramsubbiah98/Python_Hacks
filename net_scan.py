import scapy.all as sc
import socket

# Developed by Hari
"""
     1.starting process is to obtain ip address along with mac address to manipulating any device
     2.sending network packets, Recieving data with arping,storing in our system
     3.Hos
"""

def scan(ip_range):
    try:
        print(f"Starting ARP scan on {ip_range}")
        answered, unanswered = sc.arping(ip_range)
        with open("net.txt", "w") as fh:
            for sent, received in answered:
                ip_addr = received.psrc
                mac_addr = received.hwsrc
                try:
                    hostname = socket.gethostbyaddr(ip_addr)[0]
                except socket.herror:
                    hostname = "Unknown"
                except Exception as e:
                    hostname = f"Error: {e}"
                fh.write(f"IP: {ip_addr}, MAC: {mac_addr}, Hostname: {hostname}\n")
                print(f"IP: {ip_addr}, MAC: {mac_addr}, Hostname: {hostname}")
        print("File Saved")
    except Exception as e:
        print(f"An error occurred during scanning: {e}")

if __name__ == "__main__":
    scan("192.168.230.0/24")
