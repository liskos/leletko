import ipaddress

ip = ipaddress.ip_address("222.190.122.24")
for m in range(21, 33):
    net = ipaddress.ip_network(f"222.190.120.0/{m}", 0)
    if ip in net:
        print(len(list(net)))