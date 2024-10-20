import ipaddress

k = 0
net = ipaddress.ip_network("98.116.0.0/255.252.0.0", 0)
for ip in net:
    if ip.__format__("b").count("0") % 2 == 0:
        k += 1
print(k)