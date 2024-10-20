import ipaddress

ip = ipaddress.ip_address("180.2.252.76")
for m in range(10,32):
    net = ipaddress.ip_network(f"180.2.252.76/{m}", 0)
    print(net, net.netmask)