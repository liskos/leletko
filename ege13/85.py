import ipaddress

ip = ipaddress.ip_address("48.95.137.38")
for m in range(10,32):
    net = ipaddress.ip_network(f"48.95.128.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)