file = open("26data/26-J4.txt")
n = int(file.readline())
print(n)
a = [int(x) for x in file]
a.sort(reverse=True)
s = sum(a[n//10:-n//10])
print(s)
print(a[n//10])