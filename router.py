import netifaces

def get_wifi_router_ip():
    gateways = netifaces.gateways()
    # Get the default gateway for IPv4
    default_gateway = gateways.get('default', {}).get(netifaces.AF_INET)

    if default_gateway:
        router_ip = default_gateway[0]
        return router_ip
    return None

router_ip = get_wifi_router_ip()
if router_ip:
    print(f"The IP address of the Wi-Fi router is: {router_ip}")
else:
    print("No Wi-Fi router IP address found.")
