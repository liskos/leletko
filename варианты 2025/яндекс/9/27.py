import math, turtle

def srarif(a):
    sr = 0
    k = 0
    for i1 in range(len(a)):
        for i2 in range(i1+1, len(a)):
            sr += math.dist(a[i1], a[i2])
            k += 1
    return sr / k


def clasterization(data, r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) <= r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters


def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red", "green", "blue", "pink", "orange", "yellow", "brown","black"]
    for i, claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x,y)
            turtle.dot(5,colors[i % len(colors)])
    turtle.done()

data = [list(map(float,line.split())) for line in open("27_B.txt")]
clasters = clasterization(data,20)
print([len(c) for c in clasters])
for c in clasters:
    w, h = max(x for x,y in c) - min(x for x,y in c), max(y for x,y in c) - min(y for x,y in c)
    print("w=", w,"   h=", h)
# x
def mediana(a):
    if len(a) % 2 == 1:
        return a[:len(a)//2], a[len(a)//2 +1:], a[len(a)//2]
    q = (a[len(a)//2 - 1] + a[len(a)//2])/2
    return a[:len(a)//2],a[len(a)//2 + 1:], q
clasters_new = []
for c in clasters:
    claster = []
    arg_x = sorted([x for x, y, in c])
    arg_nige, arg_vishe, q2 = mediana(arg_x)
    a1, a2, q1 = mediana(arg_nige)
    a1, a2, q3 = mediana(arg_vishe)
    iqr = q3 - q1
    left_x, pravo_x = q1 - 1.5*iqr, q3 + 1.5*iqr

    arg_y = sorted([y for x, y, in c])
    arg_nige, arg_vishe, q2 = mediana(arg_y)
    a1, a2, q1 = mediana(arg_nige)
    a1, a2, q3 = mediana(arg_vishe)
    iqr = q3 - q1
    left_y, pravo_y = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    for x, y in c:
        if left_x <= x <= pravo_x and left_y <= y <= pravo_y:
            claster.append([x, y])
    clasters_new.append(claster)
print([len(c) for c in clasters_new])
print("количество выбросов", sum([len(c) for c in clasters]) - sum([len(c) for c in clasters_new]))
ind_opas = [srarif(c)/len(c) for c in clasters_new]
print(ind_opas)
print("макс инд опасности", max(ind_opas)*100000)


