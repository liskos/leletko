def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + bin(b.count("1"))[2:]
    else:
        b = "1" + b + "00"
    return  int(b, 2)


for i in range(1, 1000):
    if f(i) > 215:
        print(i)
print(f(13))

