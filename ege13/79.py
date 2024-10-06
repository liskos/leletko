import ipaddress

ip1 = ipaddress.ip_address("161.158.136.231")
ip2 = ipaddress.ip_address("161.158.138.65")
for m in range(5, 32):
    net = ipaddress.ip_network(f"161.158.136.231/{m}", 0)
    if ip1 in net and ip2 in net:
        print(net, net.netmask)