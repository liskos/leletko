import ipaddress


def f(net):
    for ip in net:
        if ip.__format__("b")[:16].count("0") > ip.__format__("b")[16:].count("0"):
            return False
    return True


for a in range(0,256):
    net = ipaddress.ip_network(f"227.31.{a}.139/255.255.255.224", 0)
    if f(net):
        print(a, net)