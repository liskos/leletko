def f(x):
    return (x + 3), (x + 8), (x * 2)

a = [" "] * 10000

for i in range(10000):
    if i >= 333:
        a[i] = "0"

for i in range(500):
    if a[i] == " " and any(a[x] in "0" for x in f(i)):
        a[i] = "1"

for i in range(500):
    if a[i] == " " and all(a[x] in "1" for x in f(i)):
        a[i] = "2"

for i in range(500):
    if a[i] == " " and any(a[x] in "2" for x in f(i)):
        a[i] = "3"

for i in range(500):
    if a[i] == " " and all(a[x] in "13" for x in f(i)):
        a[i] = "4"

import sys
sys.stdout = open("192021.xls", mode="w")
print(*a[1:], sep="\t")
