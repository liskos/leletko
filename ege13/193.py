import ipaddress

k = 0
net = ipaddress.ip_network("154.24.165.32/255.255.255.224", 0)
for ip in net:
    if ip.__format__("b")[:16].count("1") < ip.__format__("b")[16:].count("1"):
        k += 1
print(k)