import ipaddress

k = set()
for m in range(10, 32):
    net = ipaddress.ip_network(f"111.7.92.52/{m}", 0)
    print(net, net.netmask)