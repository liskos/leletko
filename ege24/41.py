d = open("24data/k7-m3.txt").read()
s = d.replace("A", " ").replace("B", " ")
s = s.split()
r = []
k = 1
for x in s:
    if len(x) <= 4:
        print(k,len(x),"C" + "c" * (len(x)-1))
        k += 1