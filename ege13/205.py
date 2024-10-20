import ipaddress

ip1 = ipaddress.ip_address("211.188.211.49")
ip2 = ipaddress.ip_address("211.188.200.115")
for m in range(0,32):
    net = ipaddress.ip_network(f"211.188.211.49/{m}", 0)
    if ip2 in net:
        print(net, net.netmask)