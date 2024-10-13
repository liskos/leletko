import sys
sys.stdin = open("17.txt")
a = [int(input()) for x in range(6679)]

c = []
b = max([x for x in a if len(str(abs(x))) == 5 and str(x)[-1] == "7"])
for i in range(6677):
    tr = a[i:i + 3]
    d = [x for x in tr if str(x)[-2:] == "12"]
    if len(d) == 2 and sum(tr) <= b:
        c.append(sum(tr))
print(len(c) ,min(c))