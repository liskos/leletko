import ipaddress

ip = ipaddress.ip_address("156.32.140.138")
for m in range(10,32):
    net = ipaddress.ip_network(f"156.32.128.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)