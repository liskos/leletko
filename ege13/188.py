import ipaddress

k = set()
net = ipaddress.ip_network("135.221.128.0/255.255.128.0", 0)
for ip in net:
    b = ip.__format__("b").count("1")
    k.add(b)
print(min(k))