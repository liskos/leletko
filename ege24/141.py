f = open("24data/24-s1.txt")
s = f.readlines()
k = 0
for x in s:
    for i in range(len(x) - 2):
        if x[i] == 'F' and x[i + 2] == 'O':
            k += 1
            break
print(k)