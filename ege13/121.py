import ipaddress

ip = ipaddress.ip_address("133.57.64.130")
for m in range(10,32):
    net = ipaddress.ip_network(f"133.57.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)