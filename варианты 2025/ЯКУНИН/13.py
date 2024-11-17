import ipaddress

ip1 = ipaddress.ip_address("192.168.82.70")
ip2 = ipaddress.ip_address("192.168.96.54")
for m in range(10,33):
    net1 = ipaddress.ip_network(f"192.168.82.70/{m}", 0)
    net2 = ipaddress.ip_network(f"192.168.96.54/{m}", 0)
    for ip1 in net1:
        if ip1 not in net2:
            print(net2)