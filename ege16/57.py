def f(n):
    if n > 25:
        return n * n + 2 * n + 1
    if n % 2 == 0 and n <= 25:
        return 2 * f(n + 1) + f(n + 3)
    return  f(n + 2) + 3 * f(n + 5)


a = set()
for i in range(1, 1001):
    if  "0" not in  str(f(i)):
        a.add(i)
print(len(a))
