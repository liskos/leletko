import ipaddress

ip = ipaddress.ip_address("148.228.120.242")
for m in range(10,32):
    net = ipaddress.ip_network(f"148.228.112.0/{m}", 0)
    if ip in net:
        print(net, net.netmask)