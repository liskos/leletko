import ipaddress

ip1 = ipaddress.ip_address("152.217.69.70")
ip2 = ipaddress.ip_address("152.217.125.80")
for m in range(5, 32):
    net = ipaddress.ip_network(f"152.217.69.70/{m}", 0)
    if ip1 in net and ip2 in net:
        print(net, net.netmask)