def func(x,y):
    if x > y:
        return (x,y+1), (x,y+3)
    if x < y:
        return (x+1,y),(x+3,y)

a = [[" "] * 1000 for _ in range(1000)]

for i in range(1000):
    for j in range(1000):
        if i ==j:
            a[i][j] ="0"

for i in range(100):
    for j in range(100):
        if a[i][j] == " " and any(a[x][y] == "0" for x, y in func(i,j)):
            a[i][j] = "1"
for i in range(100):
    for j in range(100):
        if a[i][j] == " " and all(a[x][y] in "-1" for x, y in func(i,j)):
            a[i][j] = "2"
for i in range(100):
    for j in range(100):
        if a[i][j] == " " and any(a[x][y] == "2" for x, y in func(i,j)):
            a[i][j] = "3"
for i in range(100):
    for j in range(100):
        if a[i][j] == " " and all(a[x][y] in "-13" for x, y in func(i,j)):
            a[i][j] = "4"


import sys
sys.stdout = open("113.xls", mode="w")
for i in range(1, 1000):
    print(*a[i][1:], sep="\t")