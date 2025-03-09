def p(n):
    b = ""
    while n > 0:
        b =b + str(n%5)
        n =n // 5
    return b[::-1]


def f(n):
    b = p(n)
    if n % 2 == 0:
        b = "3" + b + str(n%5)
    else:
        b = str(n%4) + b + "4"
    return int(b,5)

r = []
print(f(13))
print(f(6))
for i in range(1,16):
    r.append(f(i))

print(max(r))