import ipaddress

ip = ipaddress.ip_address("194.162.77.94")
for m in range(10,32):
    net = ipaddress.ip_network(f"194.162.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)