a = [1]
for k in range(15):
    b = []
    for i in a:
        b.append(i+1)
        b.append(i+5)
        b.append(i*3)
    a = b.copy()
    if 111 in a:
        print(k)
        break