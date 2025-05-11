s = open("24data/24-191.txt").read()
k = 0
if s[0] != "A":
    k = k - 1
if s[-1] != "A":
    k = k -1
s = s.split("A")
for i in s:
    if i.count("B") == 0 and len(i) <= 10:
        k += 1

print(k)