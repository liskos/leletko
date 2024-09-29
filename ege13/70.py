import ipaddress

ip1 = ipaddress.ip_address("115.127.30.120")
ip2 = ipaddress.ip_address("115.127.151.120")
for m in range(5, 32):
    net = ipaddress.ip_network(f"115.127.30.120/{m}", 0)
    if ip1 in net and ip2 in net:
        print(net, net.netmask)