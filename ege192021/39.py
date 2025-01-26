def func(x):
    return (x+2), (x*2)


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

import sys
sys.stdout = open("39.xls", mode="w")
print(*a[1:], sep="\t")