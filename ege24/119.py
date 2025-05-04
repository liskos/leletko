s = open("24data/24-1.txt").read()

t = ""
maxl = 0
maxst = 0
index_prime = 0
for i in range(len(s)):
    if t == "":
        t = s[i]
    elif t[-1] > s[i]:
        t += s[i]
    else:
        t = s[i]
    if len(t) > maxl:
        maxl = len(t)
        maxst = t
        index_prime = i - len(t) + 1 + 1

print(index_prime)