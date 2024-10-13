import ipaddress

ip = ipaddress.ip_address("132.47.160.46")
for m in range(10,32):
    net = ipaddress.ip_network(f"132.47.160.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)