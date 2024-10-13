import ipaddress

ip = ipaddress.ip_address("18.168.250.32")
for m in range(10,32):
    net = ipaddress.ip_network(f"18.168.240.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)