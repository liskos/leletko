import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"92.52.42.52/{m}", 0)
    print(net, net.netmask)