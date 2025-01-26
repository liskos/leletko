import ipaddress

net = ipaddress.ip_network("158.214.121.40/255.255.255.224", 0)
for ip in net:
    print(ip)
