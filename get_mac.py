import scapy.all as sc
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-r", "--range", dest="range", help="Specify IP range to scan")
    options, _ = parser.parse_args()
    if not options.range:
        parser.error("[-] Please specify an IP range, use --help for more info.")
    return options

def scan(ip_range):
    print("Program Started")
    arp_request = sc.ARP(pdst=ip_range)
    broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = sc.srp(arp_request_broadcast, timeout=10, verbose=False)[0]

    result_list = []
    for sent, received in answered_list:
        result = {"IP Address": received.psrc, "MAC Address": received.hwsrc}
        result_list.append(result)
        print(f"IP Address: {received.psrc}, MAC Address: {received.hwsrc}")

    with open("net_scan_results.txt", "w") as file:
        for result in result_list:
            file.write(f"IP Address: {result['IP Address']}, MAC Address: {result['MAC Address']}\n")
    
    print("Results saved to net_scan_results.txt")

if __name__ == "__main__":
    options = get_arguments()
    scan(options.range)
