for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (( not x) and (not y or y) and ( not w)) or ((z == w) and (( not(x or y)) or w))
                print(x, y, z, w, "!", int(f))