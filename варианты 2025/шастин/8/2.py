for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (not z or x) and (not (x and (y == (not z))) or w)
                print(x, y, z, w, "!", int(f))