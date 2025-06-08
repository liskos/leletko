import math, turtle

def clasterization(data,r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5 <= r]
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
    colors = "green", "red", "pink", "blue", "yellow"
    for i, claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*15,y*15)
            turtle.dot(5, colors[i%len(colors)])
    turtle.done()


data = [list(map(float,line.split())) for line in open("27a.txt")]
clasters = clasterization(data,2)
pl = [len(x)/16 for x in clasters]
print(pl)
print(sum(pl)/3*1000)
mm = get_centroid(clasters[1])
mx = get_centroid(clasters[2])
print(math.dist(mm,mx)*1000)

data = [list(map(float,line.split())) for line in open("27b.txt")]
clasters = clasterization(data,2)
pl = [len(x)/16 for x in clasters]
print(pl)
print(sum(pl)/5*1000)
mm = get_centroid(clasters[0])
mx = get_centroid(clasters[-1])
print(math.dist(mm,mx)*1000)

