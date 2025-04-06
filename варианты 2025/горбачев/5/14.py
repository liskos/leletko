def f(n):
    b = ""
    while n >0:
        b =b + str(n%7)
        n = n // 7
    return b.count("6")

k =0
r = set()
for x in range(1,1000+1):
    a = 5**x + 31**31 - 46**17 - x
    if 100 < f(a) < 1000:
        k += 1
print(k)