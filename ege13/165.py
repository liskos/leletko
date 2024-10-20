import ipaddress

net = ipaddress.ip_network("202.75.38.100/255.255.128.0", 0)
k = 0
for ip in net:
    if int(ip.__format__("b")) % 4 == 0:
        k += 1
print(k)