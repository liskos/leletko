import ipaddress

ip = ipaddress.ip_address("124.32.48.131")
for m in range(10,32):
    net = ipaddress.ip_network(f"124.32.32.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)