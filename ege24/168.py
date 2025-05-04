s = open("24data/24-168.txt").read()
x = y = z = m = 0
for i in range(1,len(s)-1):
    m = max(m,i-x)
    if s[i-1] > s[i]:
        x = y = z = i
    elif s[i-1] < s[i]:
        x,y,z = y,z,i

print(m)