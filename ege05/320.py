def pr(n):
    b = ""
    while n > 0:
        b = b + str(n % 3)
        n = n // 3
    return b[::-1]

def f(n):
    b = pr(n)
    if n % 2 == 0:
        b = b + b[-2:]
    else:
        b = b + pr(sum(int(x) for x in b))
    return int(b, 3)


print(f(3))
print(f(11))
a = set()
for i in range(10, 1000):
    a.add(f(i))
x = min(a)
for i in range(10, 1000):
    if f(i) == x:
        print(i)