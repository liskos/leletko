import ipaddress

ip = ipaddress.ip_address("111.91.200.28")
for m in range(10,32):
    net = ipaddress.ip_network(f"111.91.192.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)