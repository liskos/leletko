def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = "1" + b + "00"
    else:
        b = b + bin(b.count("1"))[2:]
    return int(b, 2)


print(f(4))
print(f(13))
for i in range(1, 100):
    if f(i) > 88:
        print(f(i), i)