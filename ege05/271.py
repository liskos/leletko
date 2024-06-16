def p(n):
    a = ""
    while n > 0:
        a = a + str(n % 4)
        n = n //4
    return a[::-1]
def f(n):
    b = ""
    if n % 2 == 0:
        b = "13" + p(n) + "02"
    else:
        b = "2" + p(n) + "11"
    return int(b, 4)


a = set()
for i in range(1, 1000):
    if f(i) > 1000:
        a.add(f(i))

print(f(45))
print(min(a))