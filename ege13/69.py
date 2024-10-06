import ipaddress

ip = ipaddress.ip_address("217.138.127.144")
for m in range(10,32):
    net = ipaddress.ip_network(f"217.138.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)