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
        r += [(sum(max(abs(p2[0]-p1[0]),abs(p2[1]-p1[1])) for p2 in claster), p1)]

    return min(r)[1]

def srt(data):
    r = []
    for p1 in data:
        k = 0
        for p2 in data:
            if (p1[0] != p2[0] or p1[1] != p2[1]) and p1[0]//1 == p2[0]//1 and p1[1]//1 == p2[1]//1:
                k += 1
    return r



def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red", "green", "blue", "pink", "orange", "yellow", "brown","black"]
    for i, claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*20,y*20)
            turtle.dot(5,colors[i % len(colors)])
    turtle.done()

data = [list(map(float,line.split())) for line in open("27a.txt")]
clasters = clasterization(data,1)
clastersr = clasters[0] , clasters[1]
print([len(c) for c in clasters])
print(clastersr)
visual(clastersr)
aug = srt(data)
print(aug)
print(max(aug)*1000, sum(aug)/len(aug)*1000)