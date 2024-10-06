import ipaddress

ip1 = ipaddress.ip_address("121.171.5.70")
ip2 = ipaddress.ip_address("121.171.29.68")
for m in range(5, 32):
    net = ipaddress.ip_network(f"121.171.5.70/{m}", 0)
    if ip1 in net and ip2 in net:
        print(net, net.netmask)