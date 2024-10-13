import ipaddress

ip = ipaddress.ip_address("149.112.71.192")
for m in range(10,32):
    net = ipaddress.ip_network(f"149.112.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)