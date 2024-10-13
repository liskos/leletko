import ipaddress

ip = ipaddress.ip_address("241.185.253.57")
for m in range(10,32):
    net = ipaddress.ip_network(f"241.185.252.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)