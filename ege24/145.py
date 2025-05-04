s = open("24data/24-j7.txt").read()
t = s[0]
r = []
k = 0
for i in range(1,len(s)):
    if s[i] == "\n" or int(t[-1]) % 2 == int(s[i]) % 2:
        t += s[i]
    else:
        r.append(len(t))
        t = s[i]

print(max(r))