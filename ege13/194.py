import ipaddress

k = 0
net = ipaddress.ip_network("186.135.80.0/255.255.252.0", 0)
for ip in net:
    if ip.__format__("b")[:16].count("1") > ip.__format__("b")[16:].count("1"):
        k += 1
print(k)