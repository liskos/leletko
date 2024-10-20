import ipaddress

k = 0
net = ipaddress.ip_network("99.64.0.0/255.192.0.0", 0)
for ip in net:
    if ip.__format__("b")[-2:] == "11":
        k += 1
print(k)