def f(a):
    b = bin(a)[2:]
    b = b.zfill(8)
    i = b.rfind("1")
    t = ""
    for k in range(i):
        if b[k] == "1":
            t += "0"
        else:
            t += "1"
    return int(t + b[i:], 2)


print(f(211))
