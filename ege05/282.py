def s(n):
    s = 0
    while n > 0:
        s = s +  n % 10
        n = n // 10
    return bin(s)[2:]


def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + str(s(n))
    else:
        b = "1" + b + "00"
    return  int(b, 2)


for i in range(1, 1000):
    if f(i) > 215:
        print(i)
print(f(13))

