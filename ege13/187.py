import ipaddress

k = set()
net = ipaddress.ip_network("204.252.0.0/255.255.0.0", 0)
for ip in net:
    b = ip.__format__("b").count("1")
    k.add(b)
print(max(k))