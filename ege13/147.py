import ipaddress

ip1 = ipaddress.ip_address("191.131.175.201")
ip2 = ipaddress.ip_address("191.131.160.170")
for m in range(10,32):
    net1 = ipaddress.ip_network(f"191.131.175.201/{m}", 0)
    net2 = ipaddress.ip_network(f"191.131.160.170/{m}", 0)
    if ip1 not in net2 and ip2 not in net1:
        print(net1, net2, net1.netmask)