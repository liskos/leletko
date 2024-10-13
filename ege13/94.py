import ipaddress

ip = ipaddress.ip_address("203.155.64.98")
for m in range(10,32):
    net = ipaddress.ip_network(f"203.155.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)