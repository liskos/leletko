import ipaddress

ip1 = ipaddress.ip_address("61.58.73.42")
ip2 = ipaddress.ip_address("61.58.75.136")
for m in range(5, 32):
    net = ipaddress.ip_network(f"61.58.73.42/{m}", 0)
    if ip1 in net and ip2 in net:
        print(net, net.netmask)