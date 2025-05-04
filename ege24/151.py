s = open("24data/24-j9.txt").read()

k = 0
for i in range(len(s)-4):
    if s[i:i+5] == s[i:i+5][::-1]:
        k += 1

print(k)