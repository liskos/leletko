import ipaddress

ip = ipaddress.ip_address("145.192.94.230")
for m in range(10,32):
    net = ipaddress.ip_network(f"145.192.80.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)