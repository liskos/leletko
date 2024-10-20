import ipaddress

k = 0
net = ipaddress.ip_network("213.0.0.0/255.192.0.0", 0)
for ip in net:
    if "111" in ip.__format__("b"):
        k += 1
print(k)