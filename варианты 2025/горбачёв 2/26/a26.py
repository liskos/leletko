def func(s):
    import sys
    sys.stdin = open(s)
    n = int(input())
    a = []
    for _ in range(n):
        art, cena, stat = map(int, input().split())
        a.append([art, cena, stat])
    sr = (sum([x[1] for x in a]))/ n
    dorog = [x for x in a if x[1] > sr]
    desh = [x for x in a if x[1] < sr]

    slovar = dict()
    for x in a:
        slovar[x[0]] = slovar.get(x[0], 0) + 1
    print(slovar)
    return sr, 0



if __name__ == "__main__":
    print(func("26.txt"))
