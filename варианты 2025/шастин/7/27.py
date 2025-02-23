def clasterization(data):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 < 400]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [(sum(((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5  for p2 in claster), p1)]
    return min(r)[1]

data = [list(map(int,line.split())) for line in open("27_A.txt")]
clasters = clasterization(data)
print([len(c) for c in clasters])
centroid = [get_centroid(c) for c in clasters]
print(centroid)
x,y = sum(p[0] for p in centroid ) / len(centroid), sum(p[1] for p in centroid) / len(centroid)
print(x,y)
data = [list(map(int,line.split())) for line in open("27_B.txt")]
clasters = clasterization(data)
print([len(c) for c in clasters])
centroid = [get_centroid(c) for c in clasters]
print(centroid)
x,y = sum(p[0] for p in centroid ) / len(centroid), sum(p[1] for p in centroid) / len(centroid)
print(x,y)