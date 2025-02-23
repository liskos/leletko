import turtle,math

def clasterization(data,r):
    clasters = []
    while data: # перебираем все звёзды, пока они есть в массиве
        clasters.append([data.pop()]) # начинаем новый кластер из одной звезды, удаляя её из дата
        for p1 in clasters[-1]: # перебираем звёзды последнего кластера
            sosedi = [p2 for p2 in data if math.dist(p1,p2) < r] # ищем звезды ближе чел r к нашей звезде p1
            clasters[-1].extend(sosedi) #добавляем соседей в последний кластер
            for p in sosedi: # перебираем всех соседей
                data.remove(p) # и удаляем их из дата
    return clasters

def get_centroid(claster):
    r = []
    for p1 in claster: # перебираем все звезды кластера
        r += [(sum(math.dist(p1,p2) for p2 in claster), p1)] # составляем массив сумм растояний от этой звезды до всех звезд
    return min(r)[1] # выводим точку с мин расстоянием


data = [list(map(float,line.split())) for line in open("27_A.txt")]
clasters = clasterization(data, 1)
print([len(c) for c in clasters])
x, y = get_centroid(clasters[-1])
print(x*10000,y*10000)

data = [list(map(float,line.split())) for line in open("27_B.txt")]
clasters = clasterization(data, 1)
print([len(c) for c in clasters])
m = min([len(c) for c in clasters if len(c) >= 20])
claster = [c for c in clasters if len(c) == m]
x, y = get_centroid(claster)
print(x*10000,y*10000)
