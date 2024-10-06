import ipaddress

ip = ipaddress.ip_address("248.228.60.240")
for m in range(10,32):
    net = ipaddress.ip_network(f"248.228.56.0/{m}", 0)
    if ip in net:
        print(net, net.netmask)