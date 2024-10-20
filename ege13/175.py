import ipaddress

ip = ipaddress.ip_address("134.73.209.97")
for m in range(10,32):
    net = ipaddress.ip_network(f"134.73.209.97/{m}", 0)
    print(net, net.netmask)