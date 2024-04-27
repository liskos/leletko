def f(x):
    s1 = x % 7
    s2 = x % 2
    s3 = x % 5
    return str(s1) + str (s2) + str(s3)

print(f(55))
a = set()
for i in range (10, 100):
    if f(i) == "312":
        a.add(i)
print(a, len(a))
