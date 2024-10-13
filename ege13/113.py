import ipaddress

ip = ipaddress.ip_address("169.97.112.115")
for m in range(10,32):
    net = ipaddress.ip_network(f"169.97.112.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)