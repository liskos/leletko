def f(x):
    for _ in range(5):
        if str(x) == str(x)[::-1]:
            return True
        x = x + int(str(x)[::-1])
    return str(x) == str(x)[::-1]


a = []
for i in range(100, 201):
    if f(i):
      a.append(i)
print(len(a))