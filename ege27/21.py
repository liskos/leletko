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

def get_ros(a,b):
    r = []
    for p1 in a:
        for p2 in b:
            r.append(math.dist(p1,p2))
    return min(r)*10000, max(r)*10000


def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red", "green", "blue", "pink", "orange", "yellow", "brown","black"]
    for i, claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*20,y*20)
            turtle.dot(5,colors[i % len(colors)])
    turtle.done()

data = [list(map(float,line.split())) for line in open("27data/27-21a.txt")]
clasters = clasterization(data,1)
print([len(c) for c in clasters])
print(get_ros(clasters[0], clasters[1]))
data = [list(map(float,line.split())) for line in open("27data/27-21b.txt")]
clasters = clasterization(data,1)
print([len(c) for c in clasters])
vsed = [get_ros(clasters[0],clasters[1]), get_ros(clasters[1],clasters[2]), get_ros(clasters[0], clasters[2])]
visual(clasters)
r = []
for x,y in vsed:
    r.append(x)
    r.append(y)
print(min(r), max(r))