for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            f = (not x or y) and (w or (not w))
            print(x, y, w, "!", int(f))