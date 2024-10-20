import ipaddress


def f(net):
    for ip in net:
        if ip.__format__("b")[:16].count("0") >= ip.__format__("b")[16:].count("0"):
            return False
    return True


for a in range(0,256):
    net = ipaddress.ip_network(f"159.242.{a}.223/255.255.254.0", 0)
    if f(net):
        print(a, net)