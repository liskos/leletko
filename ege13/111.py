import ipaddress

ip = ipaddress.ip_address("138.75.241.160")
for m in range(10,32):
    net = ipaddress.ip_network(f"138.75.240.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)