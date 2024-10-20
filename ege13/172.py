import ipaddress

ip = ipaddress.ip_address("151.168.147.193")
for m in range(10,32):
    net = ipaddress.ip_network(f"151.168.147.193/{m}", 0)
    print(net)