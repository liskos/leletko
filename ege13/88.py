import ipaddress

ip = ipaddress.ip_address("63.132.140.28")
for m in range(10,32):
    net = ipaddress.ip_network(f"63.132.140.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)