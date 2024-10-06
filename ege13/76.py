import ipaddress

ip1 = ipaddress.ip_address("211.115.61.154")
ip2 = ipaddress.ip_address("211.115.59.137")
for m in range(5, 32):
    net = ipaddress.ip_network(f"211.115.61.154/{m}", 0)
    if ip1 in net and ip2 in net:
        print(net, net.netmask)