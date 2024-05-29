import socket 

def get_local_ip():
    try:
         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         s.connect(("8.8.8.8", 80))
         local_ip = s.getsockname()[0]
         s.close()
         return local_ip
    except Exception as e:
         return f"error:{e}"
    

if __name__=="__main__":
        ip_address = get_local_ip()
        print(f"Local IP address: {ip_address}")