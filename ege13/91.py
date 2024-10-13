import ipaddress

ip = ipaddress.ip_address("108.87.113.106")
for m in range(10,32):
    net = ipaddress.ip_network(f"108.87.112.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)