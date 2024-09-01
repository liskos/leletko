for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f =  not((x == y) or (y == w) or (w == z)) or ( x and (not y))
                print(x, y, z, w, "!", int(f))
