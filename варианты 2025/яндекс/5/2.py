for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = not((( not (((w and x) == x) or 1) or z) or (not x)) and y)
                print(x, y, z, w, "!", int(f))