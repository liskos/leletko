import ipaddress

k = 0
net = ipaddress.ip_network("143.198.224.0/255.255.240.0", 0)
for ip in net:
    if ip.__format__("b").count("0") % 2 != 0:
        k += 1
print(k)