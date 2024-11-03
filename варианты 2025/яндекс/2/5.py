def pe(n):
    b = ""
    while n > 0:
        b = b + str(n%5)
        n = n // 5
    return b[::-1]

def f(n):
    b = pe(n)
    if n % 25 == 0:
        b = b[-3:] + b
    else:
        b = b + pe(n%25)
    return int(b, 5)

print(f(25))
print(f(26))
for i in range(1, 1000):
    if f(i) > 10000:
        print(i)
        break
