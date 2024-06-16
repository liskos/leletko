def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = "11" + b + "11"
    else:
        b =  "1" + b + "0"
    return int(b, 2)

a = set()
for i in range(1, 1000):
    if f(i) < 126:
        a.add(f(i))
print(f(14))
print(max(a))