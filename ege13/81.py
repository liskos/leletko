import ipaddress

ip = ipaddress.ip_address("215.181.200.27")
for m in range(10,32):
    net = ipaddress.ip_network(f"215.181.192.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)