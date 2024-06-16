def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = "1" + b + "11"
    else:
        b = "11" + b + "0"
    return int(b, 2)


a = set()
for i in range(1, 1000):
    if 500 <= f(i) <= 1000:
        a.add(i)
print(f(13))
print(len(a))