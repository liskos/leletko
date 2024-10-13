import ipaddress

ip = ipaddress.ip_address("163.232.136.60")
for m in range(10,32):
    net = ipaddress.ip_network(f"163.232.136.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)