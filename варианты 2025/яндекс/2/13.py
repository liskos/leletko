import ipaddress

ip = ipaddress.ip_address("20.24.110.42")
for m in range(10,32):
    net = ipaddress.ip_network(f"20.24.96.0/{m}", 0)
    if ip in net:
        print(net, net.netmask)