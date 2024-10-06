import ipaddress

net = ipaddress.ip_network("192.111.223.1/255.255.255.192", 0)
print(len(list(net.hosts())))