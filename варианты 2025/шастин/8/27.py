import math,turtle

def clasterization(data,r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if math.dist(p1, p2) <= r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters


def get_center(claster):
    r = []
    for p1 in claster:
        r += [(sum(math.dist(p1, p2) for p2 in claster), p1)]
    return min(r)[1]

def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red", "green", "black", "yellow", "pink"]
    for i, claster in enumerate(clasters):
        for x, y in claster:
            turtle.goto(x*20 , y*20)
            turtle.dot(3, colors[i % len(colors)] )
    turtle.done()


def get_center_trans(data,centers):
    r = []
    for p1 in data:
        r += [(sum(math.dist(p1, p2) for p2 in centers), p1)]
    return min(r)[1]

data = [ list(map(float, line.split())) for line in open("27_A.txt")]
clasters = clasterization(data.copy(),0.4)
print(clasters)
print([len(c) for c in clasters])
visual(clasters)
centers = [get_center(c) for c in clasters]
print(centers)
x, y = get_center_trans(data, centers)
print(x * 10000, y * 10000)

data = [ list(map(float, line.split())) for line in open("27_B.txt")]
clasters = clasterization(data.copy(),0.1)
centers = [get_center(c) for c in clasters]
x, y = get_center_trans(data, centers)
print(x * 10000, y * 10000)
