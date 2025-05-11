s = open("24data/24-191.txt").read()
k = 0
s = s.replace("A", " ")
s = s.split()
for i in s:
    if "B" in i:
        i = i.split("B")
        x = i[0]
        if len(x) >= 18:
            k += 1

print(k)