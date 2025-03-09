import math,turtle
from dbm import error


def clasterizatoin1(data):
    clasters = [[], [], []]
    for x,y in data:
        if x < 5:
            clasters[0].append([x,y])
        elif y > 5:
            clasters[1].append([x,y])
        else:
            clasters[2].append([x,y])
    return clasters

def clasterizatoin2(data):
    clasters = [[], [], [], [], []]
    for x,y in data:
        alf = math.atan((y-10) / (x - 10)) * 180 / math.pi
        if x > 10 and alf > 45:
            clasters[0].append([x,y])
        elif x > 10 and 0 < alf < 45:
            clasters[1].append([x,y])
        elif x > 10 and alf < 0:
            clasters[2].append([x,y])
        elif x < 10 and alf > 45:
            clasters[3].append([x,y])
        elif x < 10 and 0 < alf < 45:
            clasters[4].append([x,y])
        else:
            print("error",x,y)
    return clasters

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [(sum(((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5 for p2 in claster), p1)]
    return min(r)[1]

def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = "green", "red", "pink", "blue", "yellow"
    for i,claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*20,y*20)
            turtle.dot(5,colors[i%len(colors)])
    turtle.done()

data = [list(map(float,line.split())) for line in open("27data/27-63a.txt")]
clasters = clasterizatoin1(data)
print([len(c) for c in clasters])
centrs = [get_centroid(c) for c in clasters]
x,y = [sum(p[0] for p in centrs) / len(centrs), sum(p[1] for p in centrs) / len(centrs)]
print(x*100000,y*100000)

data = [list(map(float,line.split())) for line in open("27data/27-63b.txt")]
clasters = clasterizatoin2(data)
print([len(c) for c in clasters])
visual(clasters)
centrs = [get_centroid(c) for c in clasters]
x,y = [sum(p[0] for p in centrs) / len(centrs), sum(p[1] for p in centrs) / len(centrs)]
print(x*100000,y*100000)