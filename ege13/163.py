import ipaddress

net = ipaddress.ip_network("184.178.54.144/255.255.255.240", 0)
k = 0
for ip in net:
    if "111" in ip.__format__("b"):
        k += 1
print(k)