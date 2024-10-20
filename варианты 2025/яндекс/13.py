import ipaddress

net = ipaddress.ip_network("10.112.0.0/255.248.0.0", 0)
k = 0
for ip in net:
    if ip.__format__("b").count("1") % 3 == 0:
        k += 1
print(k)
