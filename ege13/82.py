import ipaddress

ip = ipaddress.ip_address("15.51.208.15")
for m in range(10,32):
    net = ipaddress.ip_network(f"15.51.192.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)