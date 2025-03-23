def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = "10" + b
    else:
        b = "1" + b + "01"
    return int(b, 2)


print(f(4))
print(f(5))
r = []
for i in range(1,13):
    r.append(f(i))

print(max(r))