import ipaddress

ip1 = ipaddress.ip_address("176.213.225.119")
ip2 = ipaddress.ip_address("176.213.195.58")
for m in range(10,32):
    net = ipaddress.ip_network(f"176.213.225.119/{m}", 0)
    if ip2 in net:
        k = 0
        for ip in net:
            if ip.__format__("b").count("1") % 2 == 0:
                k += 1
    print(k)