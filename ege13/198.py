import ipaddress


ip = ipaddress.ip_address("243.46.4.198")
def f(net):
    for ip in net:
        if ip.__format__("b")[:16].count("0") > ip.__format__("b")[16:].count("0"):
            return False
    return True


for m in range(8,32):
    net = ipaddress.ip_network(f"243.46.4.198/{m}", 0)
    if f(net) and ip in net:
        print(m, net, net.netmask)