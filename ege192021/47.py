def func(x):
    return (x+1), (x*3), (x*2)


a = [" "] * 200

for i in range(200):
    if i > 60:
        a[i] = "-1"
    if 36 <= i <= 60:
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

print([x for x in range(200) if a[x] == "2"])
print([x for x in range(200) if a[x] == "3"])
print([x for x in range(200) if a[x] == "4"])

import sys
sys.stdout = open("47.xls", mode="w")
print(*a[1:], sep="\t")