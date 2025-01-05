def p(n):
    n = int(n)
    s = 1
    while n > 0:
        if (n % 10) % 2 != 0:
            s = s * (n%10)
        n = n // 10
    return s

def f(n):
    s = str(n)
    while "55" in s or "150" in s or "555" in s:
        if "55" in s:
            s = s.replace("55", "615", 1)
        if "150" in s:
            s = s.replace("150", "5950", 1)
        if "555" in s:
            s = s.replace("555", "50", 1)
    return s

for i in range(3, 10000):
    b = "0" + "5" * i
    if p(f(b)) > 100000:
        print(i)
        break