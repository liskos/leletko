import ipaddress

ip1 = ipaddress.ip_address("154.63.206.129")
ip2 = ipaddress.ip_address("154.63.100.75")
for m in range(10,32):
    net = ipaddress.ip_network(f"154.63.206.129/{m}", 0)
    if ip2 in net:
        k = 0
        for ip in net:
            if ip.__format__("b").count("1") % 2 == 0:
                k += 1
    print(k)