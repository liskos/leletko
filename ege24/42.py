d = open("24data/k7-m4.txt").read()
d = d[::-1]
s = d.replace("A", " ").replace("B", " ")
s = s.split()
r = []
k = 1
for x in s:
    if len(x) >= 6:
        print(k,len(x),"c" * (len(x)-1) + "C")
        k += 1