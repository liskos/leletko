import math, turtle

def clasterization(data, r):
    clasters = []
    while data: # перебираем все точки в неотобранном массиве
        clasters.append([data.pop()]) # начинаем новый кластер
        for p1 in clasters[-1]: # перебираем звезды последнего кластера
            sosedi = [p2 for p2 in data if math.dist(p1,p2) <= r]   # находим всех соседей звезд последнего кластера
            clasters[-1].extend(sosedi)  # найденых соседей добавляем в последний кластер
            for p in sosedi:  # удаляем из неотобранных звезд всех отобранных соседей
                data.remove(p)
    return clasters

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [(sum(math.dist(p1, p2) for p2 in claster), p1)]
    return min(r)[1]


def visual(clasters):
    turtle.up()  # подними хвост
    turtle.tracer(0)  # не анимируй
    colors = ["red", "green", "blue", "pink", "orange", "yellow", "brown","black"]
    for i, claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*20,y*20)  # перейди в точку x y масштаб 10
            turtle.dot(5,colors[i % len(colors)])  # поставь точку размер 5 с цветом
    turtle.done() # ожидай закрытие окна

data = [list(map(float,line.split())) for line in open("27data/27-1a.txt")]
clasters = clasterization(data,0.65)
print(clasters)
print([len(c) for c in clasters])
centrs = [get_centroid(c) for c in clasters]
print(centrs)
x, y = sum(p[0] for p in centrs) / len(centrs), sum(p[1] for p in centrs) / len(centrs)
print(x*10000, y*10000)
data = [list(map(float,line.split())) for line in open("27data/27-1b.txt")]
clasters = clasterization(data,0.65)
print(clasters)
print([len(c) for c in clasters])
visual(clasters)
centrs = [get_centroid(c) for c in clasters]
print(centrs)
x, y = sum(p[0] for p in centrs) / len(centrs), sum(p[1] for p in centrs) / len(centrs)
print(x*10000, y*10000)