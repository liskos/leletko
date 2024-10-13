import ipaddress

ip = ipaddress.ip_address("221.117.97.115")
for m in range(10,32):
    net = ipaddress.ip_network(f"221.117.96.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)