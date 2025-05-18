import ipaddress

net = ipaddress.ip_network("203.68.128.0/255.255.192.0", 0)
k = 0
for ip in net:
    if ip.__format__("b").count("1") % 7 != 0:
        k += 1

print(k)