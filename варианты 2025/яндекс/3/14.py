def f(n):
    b = ""
    while n > 0:
        b = b + str(n % 9)
        n = n // 9
    return b.count("0")

b = []
for i in range(0, 1951):
    b.append(f(72070+7400-i))

print(max(b))