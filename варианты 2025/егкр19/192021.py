def f(x):
    return x+2,x+5,x*2

a = [" "] * 300

for i in range(300):
    if i >= 128:
        a[i] = "0"

for i in range(300):
    if a[i] == " " and any(a[x] == "0" for x in f(i)):
        a[i] = "1"

for i in range(300):
    if a[i] == " " and all(a[x] == "1" for x in f(i)):
        a[i] = "2"

for i in range(300):
    if a[i] == " " and any(a[x] == "2" for x in f(i)):
        a[i] = "3"

for i in range(300):
    if a[i] == " " and all(a[x] in "13" for x in f(i)):
        a[i] = "4"


import sys
sys.stdout = open("192021.xls", mode="w")
print(*a[1:], sep="\t")