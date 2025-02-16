def func(x):
    return (x+4), (x+2), (x*3)


a = [" "] * 400

for i in range(400):
    if i >= 82:
        a[i] = "0"


for i in range(100):
    if a[i] == " " and any(a[x] in "0" for x in func(i)):
        a[i] = "1"

for i in range(100):
    if a[i] == " " and all(a[x] in "-1" for x in func(i)):
        a[i] = "2"

for i in range(100):
    if a[i] == " " and any(a[x] in "2" for x in func(i)):
        a[i] = "3"

for i in range(100):
    if a[i] == " " and all(a[x] in "-13" for x in func(i)):
        a[i] = "4"

import sys
sys.stdout = open("128.xls", mode="w")
print(*a[1:], sep="\t")