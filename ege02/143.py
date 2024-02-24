for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = x and ( y and z or z and w or y and not w)
                if f:
                    print(x, y, z, w, "!", int(f))