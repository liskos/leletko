import ipaddress

k = 0
p = 0
net = ipaddress.ip_network("140.116.194.0/255.255.240.0", 0)
for ip in net:
    if all(ip.packed[i].__format__("b")[-1] == "0" for i in range(4)):
        k += 1
        print(ip.__format__("b"))
    if ip.packed[0].__format__("b")[-1] == "0" and  ip.packed[1].__format__("b")[-1] == "0":
        if ip.packed[2].__format__("b")[-1] == "0" and ip.packed[3].__format__("b")[-1] == "0":
            p = p + 1
print(k)
print(p)