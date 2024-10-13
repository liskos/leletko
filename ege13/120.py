import ipaddress

ip = ipaddress.ip_address("199.92.65.189")
for m in range(10,32):
    net = ipaddress.ip_network(f"199.92.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)