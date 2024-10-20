import ipaddress

ip1 = ipaddress.ip_address("154.63.206.129")
ip2 = ipaddress.ip_address("154.63.100.75")
for m in range(0,32):
    net = ipaddress.ip_network(f"154.63.206.129/{m}", 0)
    if ip2 not in net:
        print(net, net.netmask)