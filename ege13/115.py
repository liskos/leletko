import ipaddress

ip = ipaddress.ip_address("76.155.48.2")
for m in range(10,32):
    net = ipaddress.ip_network(f"76.155.48.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)