import ipaddress

ip = ipaddress.ip_address("124.145.64.28")
for m in range(10,32):
    net = ipaddress.ip_network(f"124.145.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)