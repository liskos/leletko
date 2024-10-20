import ipaddress

net = ipaddress.ip_network("211.48.136.64/255.255.255.224", 0)
k = 0
for ip in net:
    if ip.__format__("b")[-2:] == "11":
        k += 1
print(k)