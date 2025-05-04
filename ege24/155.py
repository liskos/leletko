s = open("24data/24-153.txt").read()
k=0
r= []
for i in range(len(s)-3):
    if s[i] == "A":
        for x in range(i,len(s)):
            if s[i] == "A" and s[x] == "F" and x-i > 1:
                r.append(x-i+1)
                break
print(min(r))