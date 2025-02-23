def v(n):
    b = ""
    while n > 0:
        b =b + str(n%8)
        n = n // 8
    return b[::-1]

def f(n):
    b = v(n)
    if n % 2 == 0:
        b = b.replace("1", "2").replace("3", "2").replace("5", "2").replace("7", "2")
    else:
        b = "3" + b[1:-1] + "3"
    return int(b, 8)

print(f(9))
print(f(12))
r = []
for i in range(1,10000):
    if f(i) < 300:
        r.append(f(i))

print(max(r))