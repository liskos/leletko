def sh(n):
    s = ""
    while n > 0:
        s = str(n % 6) + s
        n = n // 6
    return s

def sh1(n):
    s = []
    while n > 0:
        s.append(n % 6)
        n = n // 6
    return s[::-1]

def sh2(n):
    s = ""
    t = "012345"
    while n > 0:
        s = t[n % 6] + s
        n = n // 6
    return s


print(sh(125))
print(sh1(125))
print(sh2(125))