import ipaddress


def f(net):
    for ip in net:
        if ip.__format__("b")[:16].count("1") <= ip.__format__("b")[16:].count("1"):
            return False
    return True


for a in range(0,256):
    net = ipaddress.ip_network(f"196.233.{a}.52/255.255.255.248", 0)
    if f(net):
        print(a, net)