import  sys, f27
sys.stdin = open("27a.txt")
kl_a = []
kl_b = []
for _ in range(995):
    x,y = map(float, input().split())
    if x < 6:
        kl_a.append([x, y])
    else:
        kl_b.append([x, y])
xa, ya = f27.funk(kl_a)
xb, yb = f27.funk(kl_b)
print((xa + xb)/2 * 100, (ya + yb) / 2 * 100)
#597 432