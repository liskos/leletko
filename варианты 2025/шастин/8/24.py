s = open("24.txt").read()
t = ""
m = 0
for i in s:
    t += i
    while not(t.count("WWF") <= 120 and "WSFWW" not in t):
        t = t[1:]
    m = max(m,len(t))

print(m)