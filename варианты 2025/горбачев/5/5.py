def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = "101" + b[3:]
    else:
        b = b[:-3] + "111"
    return int(b,2)

print(f(6))
print(f(13))
r = []
for i in range(7,34+1):
    r.append(f(i))

print(max(r))