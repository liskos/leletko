k = 0
for a in range(1,1000):
    if all((x % a == 0) or (not (x in range(170,221)) or (not (x % 24 == 0))) for x in range(1,1000)):
        k += 1
print(k)