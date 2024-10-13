import ipaddress

ip = ipaddress.ip_address("154.112.144.160")
for m in range(10,32):
    net = ipaddress.ip_network(f"154.112.144.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)