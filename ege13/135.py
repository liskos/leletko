import ipaddress

ip1 = ipaddress.ip_address("151.172.115.121")
ip2 = ipaddress.ip_address("151.172.115.156")
for m in range(10,32):
    net1 = ipaddress.ip_network(f"151.172.115.121/{m}", 0)
    net2 = ipaddress.ip_network(f"151.172.115.156/{m}", 0)
    if ip1 not in net2 and ip2 not in net1:
        print(net1, net2)