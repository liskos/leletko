import ipaddress

ip = ipaddress.ip_address("208.207.230.65")
for m in range(10,32):
    net = ipaddress.ip_network(f"208.207.224.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)