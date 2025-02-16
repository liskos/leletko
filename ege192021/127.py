def func(x):
    return (x+1), (x+3), (x*4)


a = [" "] * 1000

for i in range(1000):
    if i >= 111:
        a[i] = "0"


for i in range(200):
    if a[i] == " " and any(a[x] in "0" for x in func(i)):
        a[i] = "1"

for i in range(200):
    if a[i] == " " and all(a[x] in "-1" for x in func(i)):
        a[i] = "2"

for i in range(200):
    if a[i] == " " and any(a[x] in "2" for x in func(i)):
        a[i] = "3"

for i in range(200):
    if a[i] == " " and all(a[x] in "-13" for x in func(i)):
        a[i] = "4"

import sys
sys.stdout = open("127.xls", mode="w")
print(*a[1:], sep="\t")