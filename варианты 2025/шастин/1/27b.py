import  sys, f27
sys.stdin = open("27b.txt")
kl_a = []
kl_b = []
kl_c = []
for _ in range(9900):
    x,y = map(float, input().split())
    if x < 4 and y > 2:
        kl_a.append([x, y])
    elif y < 2:
        kl_b.append([x, y])
    else:
        kl_c.append([x, y])
xa, ya = f27.funk(kl_a)
xb, yb = f27.funk(kl_b)
xc, yc = f27.funk(kl_c)
print((xa + xb + xc)/3 * 100, (ya + yb + yc) / 3 * 100)
#597 432
#408 352