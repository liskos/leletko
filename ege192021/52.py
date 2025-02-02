def func(x):
    return (x+100), (x*2)


a = [" "] * 10000

for i in range(10000):
    if i >= 1000:
        a[i] = "0"

for i in range(1000):
    if a[i] == " " and any(a[x] == "0" for x in func(i)):
        a[i] = "1"

for i in range(1000):
    if a[i] == " " and all(a[x] == "1" for x in func(i)):
        a[i] = "2"

for i in range(1000):
    if a[i] == " " and any(a[x] == "2" for x in func(i)):
        a[i] = "3"

for i in range(1000):
    if a[i] == " " and all(a[x] in "13" for x in func(i)):
        a[i] = "4"

print(len([x for x in range(1000) if a[x] == "2"]))
print(len([x for x in range(1000) if a[x] == "3"]))
print([x for x in range(1000) if a[x] == "4"])
import sys
sys.stdout = open("52.xls", mode="w")
print(*a[1:], sep="\t")