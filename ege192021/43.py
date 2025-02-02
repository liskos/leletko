def func(x):
    return (x+1), (x+2), (x+3), (x*2)


a = [" "] * 200

for i in range(200):
    if i > 33:
        a[i] = "0"

for i in range(100):
    if a[i] == " " and any(a[x] == "0" for x in func(i)):
        a[i] = "1"

for i in range(100):
    if a[i] == " " and all(a[x] == "1" for x in func(i)):
        a[i] = "2"

for i in range(100):
    if a[i] == " " and any(a[x] == "2" for x in func(i)):
        a[i] = "3"

for i in range(100):
    if a[i] == " " and all(a[x] in "13" for x in func(i)):
        a[i] = "4"

print([x for x in range(200) if a[x] == "2"])
print([x for x in range(200) if a[x] == "3"])
print([x for x in range(200) if a[x] == "4"])