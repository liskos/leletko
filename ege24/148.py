import string
s = open("24data/24-s2.txt").read()
t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
r = []
for i in t:
    r.append([s.count(f"X{i}"),i])

print(*max(r)[::-1])