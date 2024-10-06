import ipaddress

ip1 = ipaddress.ip_address("215.171.155.54")
ip2 = ipaddress.ip_address("215.171.145.37")
for m in range(5, 32):
    net = ipaddress.ip_network(f"215.171.155.54/{m}", 0)
    if ip1 in net and ip2 in net:
        print(net, net.netmask)