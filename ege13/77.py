import ipaddress

ip1 = ipaddress.ip_address("11.156.152.142")
ip2 = ipaddress.ip_address("11.156.157.39")
for m in range(5, 32):
    net = ipaddress.ip_network(f"11.156.152.142/{m}", 0)
    if ip1 in net and ip2 in net:
        print(net, net.netmask)