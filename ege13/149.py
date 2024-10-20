import ipaddress

ip1 = ipaddress.ip_address("112.74.161.2")
ip2 = ipaddress.ip_address("112.74.98.15")
for m in range(10,32):
    net1 = ipaddress.ip_network(f"112.74.161.2/{m}", 0)
    net2 = ipaddress.ip_network(f"112.74.98.15/{m}", 0)
    if ip1 not in net2 and ip2 not in net1:
        print(net1, net2, net1.netmask)