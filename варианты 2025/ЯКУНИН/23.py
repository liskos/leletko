a = {155}
for _ in range(15):
    b = set()
    for i in a:
        b.add(i+5)
        b.add(i*2)
    a = b.copy()
print(len(a))