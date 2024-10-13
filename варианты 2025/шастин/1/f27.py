def funk(kl):
    xc = 0
    yc = 0
    s = 10**10
    for x, y in kl:
        r = 0
        for x1, y1 in kl:
            r += ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
        if r < s:
            xc = x
            yc = y
            s = r
    return xc, yc