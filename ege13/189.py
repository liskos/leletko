import ipaddress

k = set()
net = ipaddress.ip_network("94.159.76.0/255.255.255.128", 0)
for ip in net:
    b = ip.__format__("b").count("0")
    k.add(b)
print(min(k))