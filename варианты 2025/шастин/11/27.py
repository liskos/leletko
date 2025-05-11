import turtle
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
        r += [(sum(((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5 for p2 in claster), p1)]
    return max(r)[1]
def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = "green", "red", "pink", "blue", "yellow"
    for i, claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*10,y*10)
            turtle.dot(5, colors[i%len(colors)])
    turtle.done()


data = [list(map(float,line.split())) for line in open("27a.txt")]
datar = data.copy()
clasters = clasterization(data,2)
print([len(c) for c in clasters])
antcentrs = [get_centroid(c) for c in clasters]
r = []
for p1 in datar:
    r += [(sum(((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5 for p2 in antcentrs), p1)]
g = max(r)[1]
print(int(abs(g[0]*10000)),int(abs(g[1]*10000)))

data = [list(map(float,line.split())) for line in open("27a.txt")]
datar = data.copy()
clasters = clasterization(data,2)
print([len(c) for c in clasters])
antcentrs = [get_centroid(c) for c in clasters]
r = []
for p1 in datar:
    r += [(sum(((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5 for p2 in antcentrs), p1)]
g = max(r)[1]
print(int(abs(g[0]*10000)),int(abs(g[1]*10000)))