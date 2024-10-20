import ipaddress

ip = ipaddress.ip_address("90.155.69.100")
for m in range(10,32):
    net = ipaddress.ip_network(f"90.155.69.100/{m}", 0)
    print(net, net.netmask)