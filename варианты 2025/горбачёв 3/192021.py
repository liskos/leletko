def func(x):
    return x-11, x//3

a = [" "] * 10000

for j in range(10000):
    if j < 91:
        a[j] = "0"

for i in range(10000):
    if a[i] == " " and any(a[x] == "0" for x in func(i)):
        a[i] = "1"

for i in range(10000):
    if a[i] == " " and all(a[x] == "1" for x in func(i)):
        a[i] = "2"

for i in range(10000):
    if a[i] == " " and any(a[x] == "2" for x in func(i)):
        a[i] = "3"

for i in range(10000):
    if a[i] == " " and all(a[x] in "13" for x in func(i)):
        a[i] = "4"

print([i for i in range(10000) if a[i] == "1"])
print("19) 2456")
z = [i for i in range(10000) if a[i] == "3"]
print("20)", max(z), min(z))
z = [i for i in range(10000) if a[i] == "4"]
print(z)
print("21)", min(z))