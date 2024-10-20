import ipaddress

net = ipaddress.ip_network("140.19.96.0/255.255.248.0", 0)
k = 0
for ip in net:
    if ip.packed[0].bit_count() == ip.packed[1].bit_count()==ip.packed[2].bit_count()==ip.packed[3].bit_count():
        k += 1
print(k)