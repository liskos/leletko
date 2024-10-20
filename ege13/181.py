import ipaddress

k = 0
net = ipaddress.ip_network("250.135.101.80/255.255.255.248", 0)
for ip in net:
    if ip.__format__("b").count("0") % 3 == 0:
        k += 1
print(k)