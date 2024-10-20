import ipaddress

net = ipaddress.ip_network("139.75.100.0/255.255.252.0", 0)
k = 0
for ip in net:
    if ip.packed[3] in [1, 3, 7, 15, 31, 63, 127, 255]:
        k += 1
print(k)