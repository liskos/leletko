import math, turtle

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

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [((abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) for p2 in claster), p1)]
    return min(r)[1]


def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red", "green", "blue", "pink", "orange", "yellow", "brown","black"]
    for i, claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*1.5,y*1.5)
            turtle.dot(5,colors[i % len(colors)])
    turtle.done()

data = [list(map(float,line.split())) for line in open("27_A.txt")]
clasters = clasterization(data,4.5)
print(len(clasters))
print([len(c) for c in clasters])
visual(clasters)