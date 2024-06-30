def pr(n):
    b = ""
    while n > 0:
        b = b + str(n % 3)
        n = n // 3
    return b[::-1]

def f(n):
    b = pr(n)
    if n % 2 == 0:
        b = b + b[-2] + b[-1]
    else:
        b = b + pr(sum(int(x, 3) for x in b))
    return int(b, 3)


print(f(3))
print(f(11))
a = set()
for i in range(3, 1000):
    a.add(f(i))
print(min(a))
for i in range(3, 1000):
    if f(i) == 10:
        print(i)