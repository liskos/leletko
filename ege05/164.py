def f(n):
    s = bin(n)[2:]
    s = str(s)
    s = s[::-1]
    s = s[s.find('1'):]
    return int(s, 2)

for n in range(1, 501):
    if f(n) == 13:
        print(n)
