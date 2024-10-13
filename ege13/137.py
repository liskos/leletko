import ipaddress

ip1 = ipaddress.ip_address("145.207.153.178")
ip2 = ipaddress.ip_address("145.207.153.165")
for m in range(10,32):
    net1 = ipaddress.ip_network(f"145.207.153.178/{m}", 0)
    net2 = ipaddress.ip_network(f"145.207.153.165/{m}", 0)
    if ip1 not in net2 and ip2 not in net1:
        print(net1, net2)