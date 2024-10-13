import ipaddress

ip = ipaddress.ip_address("118.105.136.60")
for m in range(10,32):
    net = ipaddress.ip_network(f"118.105.136.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)