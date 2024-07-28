a = [2**i for i in range(1, 29)]
print(a)
b = [i+1 for i in a]
c = []
for i in a:
    for j in b:
        if i*j <= 500000000:
            c.append(i*j)
print(sorted(c+b))
print(len(b+c))
