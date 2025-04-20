file = open("26_21424.txt")
n = int(file.readline())
k = 9
a = [int(file.readline()) for _ in range(n)]
print(f"Число коробок {n}")
a.sort(reverse=True)
print(f"Коробки: {a[:30]}")
b = [a[0]] # выбранные коробки
dostumnie_kobki = [i for i in a if b[-1] - k >= i] # доступные коробки
while dostumnie_kobki:
    b += [dostumnie_kobki[0]]
    dostumnie_kobki = [i for i in a if b[-1] - k >= i]  # доступные коробки
print(len(b), b[-1])
print(f"Выбранные коробки: {b}")