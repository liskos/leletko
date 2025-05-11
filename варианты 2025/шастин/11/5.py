def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b.replace("0", "1")
    else:
        b = "1" + b[1:].replace("1", "00")
    return int(b,2)


r = []
for i in range(1,1000):
    if f(i) <= 600:
        r.append([f(i),i])

print(max(r))


