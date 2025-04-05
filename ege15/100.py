a = {i for i in range(1, 100)} # множество чисел от 1 до 100
for i in range(1, 100):
    a.remove(i)         # удаляем одно из чисел
    if not all((x in a) or (x not in {1, 3, 7}) or ((x not in {1,2,4,5,6}) and (x in {1, 3, 7})) for x in range(1, 100)):  # если условие (для любых х верно) не выполняется, то
        a.add(i)  # добавляем его обратно
print(a)
print(len(a))
