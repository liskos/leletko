import ipaddress


ip = ipaddress.ip_address("117.157.2.8")
def f(net):
    for ip in net:
        if ip.__format__("b")[:16].count("1") < ip.__format__("b")[16:].count("1"):
            return False
    return True


for m in range(8,32):
    net = ipaddress.ip_network(f"117.157.2.8/{m}", 0)
    if f(net) and ip in net:
        print(m, net, net.netmask)