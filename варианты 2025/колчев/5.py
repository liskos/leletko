def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = "1" + b[:-2] + "11"
    if n % 3 != 0:
        b = "10" + b + "0"
    return int(b, 2)

print(f(4))
print(f(6))
r = []
for i in range(0, 1000, 2):
    if f(i) > 999:
        r.append(f(i))

print(min(r))