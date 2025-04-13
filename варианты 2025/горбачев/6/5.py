def f(n):
    b = ""
    while n > 0:
        b = b + str(n%7)
        n = n // 7
    return  b[::-1]

def g(n):
    b = f(n)
    if b.count("3") % 2 == 0:
        b = "3" + b + b[0]
    else:
        b = "6" + b + b[-1]
    return int(b,7)

print(g(11))
print(g(135))
r =[]
for i in range(1,1000):
    if g(i) < 16777:
        r.append(g(i))

print(max(r))