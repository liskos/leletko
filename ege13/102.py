import ipaddress

ip = ipaddress.ip_address("120.120.120.35")
for m in range(10,32):
    net = ipaddress.ip_network(f"120.120.120.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)