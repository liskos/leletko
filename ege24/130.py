s = open("24data/24-5.txt").read()

k = 0
for i in range(len(s)):
    if s[i] == ")":
        k += 1
    if k == 10000:
        print(i+1)
        break
