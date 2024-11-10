a = [int(x) for x in open("17data/17-273.txt")]
m = max(a)
b = []
for i in range(len(a)- 2):
    if a[i] + a[i+1] + a[i+2] < m:
        b.append(max(a[i:i+3]))
        b.append(min(a[i:i+3]))


print(len(b)//2, min(b)+max(b))