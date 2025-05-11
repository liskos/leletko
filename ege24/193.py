s = open("24data/24-191.txt").read()
k = 0
for l in [i for i in range(len(s)) if s[i]=="A"]:
    for r in range(l+1, len(s)):
        if s[r] == "A":
            break
        if s[r] == "B":
            if r - l + 1 >= 20:
                k += 1
            break

print(k)