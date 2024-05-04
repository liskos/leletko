def f(n):
    a = [int(x)  for x in str(n)]
    a[0] += 4
    a[1] += 8
    a[2] += 6
    a = sorted(a, reverse=True)
    a = [str(x) for x in a]
    return "".join(a)

print(f(835))
for i in range( 100, 1000):
    if f(i) == "13107":
        print(i)
