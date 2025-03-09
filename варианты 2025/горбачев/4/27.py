import turtle

def clasterization(data,r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5 < r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [(sum(((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5 for p2 in claster), p1)]
    return min(r)[1]

def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = "red", "blue", "yellow", "pink", "green"
    for i, claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*20,y*20)
            turtle.dot(10, colors[i%len(colors)])
    turtle.done()


data = [list(map(float,line.split())) for line in open("27a.txt")]
clasters = clasterization(data,3)
cents = [get_centroid(c) for c in clasters]
print([len(c) for c in clasters])
x,y = [sum(p[0] for p in cents) / len(cents), sum(p[1] for p in cents) / len(cents)]
print(x*100000,y*100000)
print(cents)

data = [list(map(float,line.split())) for line in open("27b.txt")]
clasters = clasterization(data,3)
cents = [get_centroid(c) for c in clasters]
visual(clasters)
print([len(c) for c in clasters])
x,y = [sum(p[0] for p in cents) / len(cents), sum(p[1] for p in cents) / len(cents)]
print(x*100000,y*100000)
print(cents)