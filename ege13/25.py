import ipaddress


ip1 = ipaddress.ip_address("145.92.137.90")
net = ipaddress.ip_network("145.92.137.88/255.255.240.0", 0)
print(ip1 in net)
for ip in net:
    print(ip.packed[3].__format__("b"))
print(len(list(net)), len(list(net.hosts())))