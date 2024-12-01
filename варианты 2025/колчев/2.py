for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (not (z == x) or w) and (not w or (y and x))
                print(x, y, z, w, "!", int(f))