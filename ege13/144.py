import ipaddress

ip1 = ipaddress.ip_address("118.187.59.255")
ip2 = ipaddress.ip_address("118.187.65.115")
for m in range(10,32):
    net1 = ipaddress.ip_network(f"118.187.59.255/{m}", 0)
    net2 = ipaddress.ip_network(f"118.187.65.115/{m}", 0)
    if ip1 not in net2 and ip2 not in net1:
        if ip1 != list(net1)[-1] and ip2 != list(net2)[-1]:
            print(net1, net2)