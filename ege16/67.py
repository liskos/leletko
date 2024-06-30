def f(n):
    if n < 3:
        return n + 1
    if n >= 3 and n % 2 == 0:
        return 100000
    if n >= 3 and n % 2 != 0:
        return f(n - 2 ) + n - 2

a =set()
for i in range(1, 1500):
    if 100 <= f(i) < 1000:
        a.add(i)
print(len(a))