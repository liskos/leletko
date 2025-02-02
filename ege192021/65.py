def func(x,y):
    return (x-1,y), (x,y-1), (x//2,y), (x,y//2)


a = [[" "] * 1000 for _ in range(1000)]

for i in range(1000):
    for j in range(1000):
        if i + j <= 18:
            a[i][j] = "0"

for i in range(500):
    for j in range(500):
        if a[i][j] == " " and any(a[x][y] == "0" for x, y in func(i,j)):
            a[i][j] = "1"
for i in range(500):
    for j in range(500):
        if a[i][j] == " " and all(a[x][y] == "1" for x, y in func(i,j)):
            a[i][j] = "2"
for i in range(500):
    for j in range(500):
        if a[i][j] == " " and any(a[x][y] == "2" for x, y in func(i,j)):
            a[i][j] = "3"
for i in range(500):
    for j in range(500):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in func(i,j)):
            a[i][j] = "4"

import sys
sys.stdout = open("65.xls", mode="w")
for i in range(1, 1000):
    print(*a[i][1:], sep="\t")