import ipaddress

ip1 = ipaddress.ip_address("156.77.32.127")
ip2 = ipaddress.ip_address("156.77.117.78")
for m in range(10,32):
    net1 = ipaddress.ip_network(f"156.77.32.127/{m}", 0)
    net2 = ipaddress.ip_network(f"156.77.117.78/{m}", 0)
    if ip1 not in net2 and ip2 not in net1:
        if ip1 != list(net1)[-1] and ip2 != list(net2)[0]:
            print(net1, net2)