def dv(n):
    s = ""
    t = "0123456789ab"
    while n > 0:
        s = t[n%12] + s
        n = n // 12
    return s

def f(s):
    a = int(s[0], 12) + int(s[2], 12)
    b = int(s[1], 12) + int(s[3], 12)
    return str(dv(max(a, b))) + str(dv(min(a, b)))

print(f("441b"))

for s1 in "12456b":
    for s2 in "12456b":
        for s3 in "12456b":
            for s4 in "12456b":
                s = s1 + s2 + s3 +s4
                if f(s) == "115":
                    print(s)