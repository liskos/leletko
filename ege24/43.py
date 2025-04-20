d = open("24data/k7-m5.txt").read()
f = d
s = ""
k = 0
for i in d:
    if i in "AB":
        if k != 0:
            s += str(k) + "c"*k + i
        else:
            s += i
        k = 0
    elif i in "C":
        k += 1
if k != 0:
    s += str(k) + "c"*k
k = 0
print(len([x for x in s.replace("B", "A").split("A") if x]))

print(d[:15], d[-15:])
print(s[:15], s[-15:])