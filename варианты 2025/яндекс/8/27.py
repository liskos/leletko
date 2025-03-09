import turtle,math

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


def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red", "green", "yellow","blue","pink","black"]
    for i,claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*5,y*5)
            turtle.dot(5,colors[i%len(colors)])
    turtle.done()

def get_maxdist(claster):
    r = []
    for p1 in claster:
        r += [math.dist(p1,p2) for p2 in claster]
    return max(r)

def get_ctoronal(claster):
    dx = max([p[0] for p in claster]) - min([p[0] for p in claster])
    dy = max([p[1] for p in claster]) - min([p[1] for p in claster])
    return max(dx,dy)


def get_data(x,y,data):
    data_new = [[p[x], p[y]] for p in data]
    return data_new

# data = [list(map(float,line.split())) for line in open("27_A(1).txt")]
# data = get_data(3,2,data)
# clasters = clasterization(data,4)
# print([len(c) for c in clasters])
# max_dists = [get_maxdist(c) for c in clasters]
# max_storonal = [get_ctoronal(c) for c in clasters]
# p = sum(max_dists) / len(max_dists)
# print(max(max_storonal) *10000, p * 10000)

data = [list(map(float,line.split())) for line in open("27_B(1).txt")]
data = get_data(4,1,data)
clasters = clasterization(data,4)
print([len(c) for c in clasters])
visual(clasters)
max_dists = [get_maxdist(c) for c in clasters]
max_storonal = [get_ctoronal(c) for c in clasters]
p = sum(max_dists) / len(max_dists)
print(max(max_storonal) *10000, p * 10000)