import math,turtle

def clasterization(data,r):
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
        r += [(sum(math.dist(p1,p2) for p2 in claster), p1)]
    return min(r)[1]

def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = "red", "pink", "green", "blue"
    for i,claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*20,y*20)
            turtle.dot(5,colors[i%len(colors)])
    turtle.done()


data = [list(map(float,line.split()))for line in open("27data/27-43a.txt")]
clasters = clasterization(data,1)
clastersr = clasters[0], clasters[1]
print([len(c) for c in clasters])
centrs = [get_centroid(c) for c in clastersr]
x,y = [sum(p[0] for p in centrs) / len(centrs), sum(p[1] for p in centrs) / len(centrs)]
print(x*100000,y*100000)

data = [list(map(float,line.split()))for line in open("27data/27-43b.txt")]
clasters = clasterization(data,0.6)
clastersr = clasters[0] , clasters[1], clasters[2]
print([len(c) for c in clasters])
visual(clasters)
centrs = [get_centroid(c) for c in clastersr]
x,y = [sum(p[0] for p in centrs) / len(centrs), sum(p[1] for p in centrs) / len(centrs)]
print(x*100000,y*100000)