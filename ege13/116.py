import ipaddress

ip = ipaddress.ip_address("151.181.88.129")
for m in range(10,32):
    net = ipaddress.ip_network(f"151.181.80.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)