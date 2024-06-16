
def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + bin(b.count("1"))[2:]
    else:
        b = "1" + b + "00"
    return  int(b, 2)


a =set()
for i in range(1, 1000):
    if 500 <= f(i) <= 700:
        a.add(i)
print(f(13))
print(len(a))
