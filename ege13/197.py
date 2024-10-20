import ipaddress


ip = ipaddress.ip_address("134.97.250.117")
def f(net):
    for ip in net:
        if ip.__format__("b")[:16].count("1") > ip.__format__("b")[16:].count("1"):
            return False
    return True


for m in range(8,32):
    net = ipaddress.ip_network(f"134.97.250.117/{m}", 0)
    if f(net) and ip in net:
        print(m, net, net.netmask)