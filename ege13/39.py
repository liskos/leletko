import ipaddress

net = ipaddress.ip_network("192.111.223.1/255.255.254.0", 0)
print(len(list(net.hosts())))