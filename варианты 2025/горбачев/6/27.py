import math, turtle

def clasterization(data, r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if max(abs(p2[0]-p1[0]),abs(p2[1]-p1[1])) <= r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters


def srt(claster):
    sum_plot = 0
    for p1 in claster:
        k = 0
        for p2 in claster:
            if max(abs(p2[0]-p1[0]),abs(p2[1]-p1[1])) <= 1:
                k += 1
        sum_plot += k
    return sum_plot/len(claster)



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
clasters = clasterization(data,0.5)
clasters = [c for c in clasters if len(c) >= 30]
print([len(c) for c in clasters])
visual(clasters)
aug = [srt(c) for c in clasters]
max_plot = max(aug)
sr_pl = sum(aug) / len(clasters)
print(max_plot*1000, sr_pl*1000)
