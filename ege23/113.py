def f(a, b, k):
    if a == b:
        r.append(k)
        return 1
    if a > b:
        return 0
    return f(a+1, b, k+1) + f(a+5, b, k+1) + f(a*3, b, k+1)

r = []
print(f(1, 227, 0))
print(min(r))