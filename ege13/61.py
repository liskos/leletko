import ipaddress

ip = ipaddress.ip_address("158.198.104.220")
for m in range(10,32):
    net = ipaddress.ip_network(f"158.198.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)