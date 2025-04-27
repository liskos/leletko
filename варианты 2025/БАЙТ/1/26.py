file = open("26.txt")
a = [list(map(int,file.readline().split())) for _ in range(9950)]
final_ot = []
not_final = []
for i in a:
    id = i[0]
    sr = sum(i[1:])/10
    k_nul = i[1:].count(0)
    if k_nul == 0:
        final_ot += [(id, sr, k_nul)]
    else:
        not_final += [(id, sr, k_nul)]
final_ot.sort(key=lambda x:(x[1], -x[0]), reverse=True)
print(final_ot)
k = len(a)//5
print(f"всего людей {len(a)}, 20% = {k}")
print(f"последний финалист {final_ot[k-1][0]}")

otbor_not = [x for x in not_final if x[2] > 5]
otbor_not.sort(key=lambda x:(x[2], x[0]))
print(otbor_not)
print(f"не прошедший отбор, с более 5 нулями: {otbor_not[0][0]}")