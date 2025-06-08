file = open("26data/26-44.txt")
n = int(file.readline())
k = 20  # количество категорий
#print(max(int(file.readline()) for _ in range(n)))
a = [[] for _ in range(k)]
for _ in range(n):
    x = int(file.readline())
    a[(x-1)//500].append(x)
print(a)
for i in range(k):
    a[i].sort()
print(a)
skidka = []
for i in range(k):
    skidka += a[i][:len(a[i])//2]
print(skidka)
print(sum(skidka)*0.5, skidka[-1]*0.5)