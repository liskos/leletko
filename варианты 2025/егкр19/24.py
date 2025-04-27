s = open("24.txt").read()
ind = [i for i in range(len(s)) if s[i:i+3] == "RSQ"]
k = 130 #130
m = 10**10
try:
    for i in range(len(ind)-130):
        left = ind[i]
        for right in range(ind[i+(k-1)] + 3, ind[i+k]+2):
            if s[right] != "Q":
                if right-left+1 < m:
                    m = right - left + 1
                    print(right-left+1, s[left:right+1])
except:
    print("---")
print(m)

