import ipaddress

k = set()
net = ipaddress.ip_network("124.8.0.0/255.248.0.0", 0)
for ip in net:
    b = ip.__format__("b").count("0")
    k.add(b)
print(max(k))