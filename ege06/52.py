import math
k = 0
for x in range(int(300*math.sin(math.pi/3))+1):
    for y in range(-300, 300):
        if - x * math.tan(math.pi/6) <= y <= x * math.tan(math.pi/6):
            k += 1
print(k)
