def f(n):
    b = ""
    while n > 0:
        b = b + str(n% 7)
        n = n // 7
    return b[::-1]


m = 0
ox = 0
for x in range(1,2031):
    a = 7**170 + 7**100 - x
    if f(a).count("0") >= m:
        m = f(a).count("0")
        ox = max(ox,x)

print(ox)