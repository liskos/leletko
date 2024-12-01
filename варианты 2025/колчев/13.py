import ipaddress

for m in range(24, 33):
    k = 0
    net = ipaddress.ip_network(f"172.16.168.0/{m}", 0)
    for ip in net:
        if ip.__format__("b").count("0") % 7 == 0:
            k += 1
    if k == 35:
        print(net.netmask)