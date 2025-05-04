s = open("24data/24-j1.txt").read()

t = "КОТ"
while t in s:
    t += "КОТ"

print(len(t)//3-1)