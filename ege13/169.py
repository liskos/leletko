import ipaddress

net = ipaddress.ip_network("117.32.0.0/255.224.0.0", 0)
k = 0
for ip in net.hosts():
    if len(set([ip.packed[0], ip.packed[1], ip.packed[2], ip.packed[3]])) == 3:
        k += 1
print(k)