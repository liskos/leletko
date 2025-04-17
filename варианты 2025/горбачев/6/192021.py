def func(x,y, r=0):
    if r == 0:
        return (x+2,y,0), (x*2,y,0), (x*3,y,1),(x,y+2,0), (x,y*2,0), (x,y*3,1)
    return (x+2,y,0), (x*2,y,0),(x,y+2,0), (x,y*2,0)


a = [[[" ", " "] for _ in range(1000)] for _ in range(1000)]

for i in range(1000):
    for j in range(1000):
        if i + j >= 132:
            a[i][j][0] = "0"
            a[i][j][1] = "0"

for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and any(a[x][y][r] == "0" for x,y,r in func(i,j,0)):
            for x,y,r in func(i,j,0):
                if r == 0:
                    a[i][j][0] = "1"
                if r == 1:
                    a[i][j][1] = "1"

for s in range(1, 100):
    if any(a[x][y][r]=="1" for x, y, r in func(31,s,0)):
        print(s)