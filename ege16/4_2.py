
def f(n):
    global d
    if n in d:
        return d[n]
    if n <= 1:
        d[n] = 2
        return 2
    d[n] = f(n - 1) + f(n - 2) + 2 * n + 4
    return f(n - 1) + f(n - 2) + 2 * n + 4


d = dict()
print(f(100))
print(d)