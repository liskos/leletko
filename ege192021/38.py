def func(x):
    a = [x*3, x+1, x+3]
    b = [x for x in a if x % 2 == 1]
    return b


a = [" "] * 200

for i in range(200):
        if i >= 51:
            a[i] = "0"

for i in range(51):
        if a[i] == " " and any(a[x] == "0" for x in func(i)):
            a[i] = "1"

for i in range(51):
        if a[i] == " " and all(a[x] == "1" for x in func(i)):
            a[i] = "2"

for i in range(51):
        if a[i] == " " and any(a[x] == "2" for x in func(i)):
            a[i] = "3"

for i in range(51):
        if a[i] == " " and all(a[x] in "13" for x in func(i)):
            a[i] = "4"

z = [i for i in range(200) if a[i] == "2"]
print("19)", min(z), z)
z = [i for i in range(200) if a[i] == "3"]
print("20)", sorted(z)[-2:], z)
z = [i for i in range(200) if a[i] == "4"]
print("21)", len(z), z)
