import ipaddress

ip1 = ipaddress.ip_address("161.137.200.35")
ip2 = ipaddress.ip_address("161.137.150.118")
for m in range(0,32):
    net = ipaddress.ip_network(f"161.137.200.35/{m}", 0)
    if ip2 not in net:
        print(net, net.netmask)