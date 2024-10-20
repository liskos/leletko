import ipaddress

net = ipaddress.ip_network("202.75.38.176/255.255.255.240", 0)
k = 0
for ip in net:
    if "000" not in ip.__format__("b") and "111" not in ip.__format__("b"):
        k += 1
print(k)