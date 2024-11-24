a = [1]
for _ in range(6):
    b = []
    for i in a:
        b.append(i+1)
        b.append(i+2)
        b.append(i*2)
    a = b.copy()
print(a.count(20))
