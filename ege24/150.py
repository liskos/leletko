import string
s = open("24data/24-s2.txt").read()
t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
r = []
for i in t:
    r.append([s.count(f"A{i}C"),i])

print(*max(r)[::-1])