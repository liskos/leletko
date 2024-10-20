import ipaddress

net = ipaddress.ip_network("216.130.64.0/255.255.192.0", 0)
k = 0
for ip in net:
    if ip.packed[0] % 2 == ip.packed[1] % 2 == ip.packed[2] % 2 == ip.packed[3] % 2 == 0:
        k += 1
print(k)