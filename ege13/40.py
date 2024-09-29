import ipaddress

net = ipaddress.ip_network("192.111.223.101/255.255.255.128", 0)
print( len(list(net.hosts())))