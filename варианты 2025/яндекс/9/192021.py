def f(x):
    return (x+3), (x+5), (x*3)


a = [" "] * 1000
for i in range(1000):
    if i >= 97 and i <= 105:
        a[i] = "0"
    if i > 105:
        a[i] = "5"

for i in range(200):
    if a[i] == " " and any(a[x] in "0" for x in f(i)):
        a[i] = "1"

for i in range(200):
    if a[i] == " " and all(a[x] in "15" for x in f(i)):
        a[i] = "2"

for i in range(200):
    if a[i] == " " and any(a[x] in "2" for x in f(i)):
        a[i] = "3"

for i in range(200):
    if a[i] == " " and all(a[x] in "153" for x in f(i)):
        a[i] = "4"

import sys

sys.stdout = open("192021.xls", mode="w")
print(*a[1:], sep="\t")
