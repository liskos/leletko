import ipaddress
net = ipaddress.ip_network("172.17.167.18/255.255.240.0",0)
for p in net:
    print(p)