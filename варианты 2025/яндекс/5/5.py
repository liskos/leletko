def s(n):
    su = 0
    while n > 0:
        if (n % 10) % 2 == 0:
            su += n % 10
        n = n // 10
    return su ** 2

def r(n):
    n = str(n)
    return (int(max(n)) - int(min(n))) ** 3

for i in range(1000,10000):
    if str(s(i)) + str(r(i)) == "4343":
        print(i)
        break
