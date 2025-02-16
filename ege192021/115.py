def func(x):
    return x+1, x+3,x+11

a = [" "] * 1000

for i in range(1000):
        if i % 10 == 0:
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


import sys
sys.stdout = open("115.xls", mode="w")
print(*a[1:], sep="\t")