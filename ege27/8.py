import math, turtle

def clasterization(data, r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if math.dist(p1,p2) <= r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [(sum(math.dist(p1, p2) for p2 in claster), p1)]
    return min(r)[1]


def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red", "green", "blue", "pink", "orange", "yellow", "brown","black"]
    for i, claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*20,y*20)
            turtle.dot(5,colors[i % len(colors)])
    turtle.done()

data = [list(map(float,line.split())) for line in open("27data/27-8a.txt")]
clasters = clasterization(data,0.6)
print([len(c) for c in clasters])
visual(clasters)
centrs = [get_centroid(c) for c in clasters]
x, y = sum(p[0] for p in centrs) / len(centrs), sum(p[1] for p in centrs) / len(centrs)
print(x*10000, y*10000)
data = [list(map(float,line.split())) for line in open("27data/27-8b.txt")]
clasters = clasterization(data,0.4)
print([len(c) for c in clasters])
centrs = [get_centroid(c) for c in clasters]
x, y = sum(p[0] for p in centrs) / len(centrs), sum(p[1] for p in centrs) / len(centrs)
print(x*10000, y*10000)