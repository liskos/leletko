def f(n):
    b = bin(n)[2:]
    if b.count("1") == b.count("0"):
        b += b[-1]
    elif b.count("1") > b.count("0"):
        b += "0"
    else:
        b += "1"
    if b.count("1") == b.count("0"):
        b += b[-1]
    elif b.count("1") > b.count("0"):
        b += "0"
    else:
        b += "1"
    if b.count("1") == b.count("0"):
        b += b[-1]
    elif b.count("1") > b.count("0"):
        b += "0"
    else:
        b += "1"
    return int(b, 2)


for i in range(1, 70):
    if f(i) % 4 ==0:
        print(i)