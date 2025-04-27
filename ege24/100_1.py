# Текстовый файл 24-2.txt содержит последовательность из строчных и заглавных букв английского алфавита и цифр,
# всего не более 10**6 символов.
# Запишите в ответе наибольшую возрастающую подпоследовательность.
# Если таких последовательностей несколько, запишите первую из них.

s = open("24data/24-2.txt").read()

t = ""
maxlen = 0
maxstroka = ""
index_prime_sumvola = 0
for i in range(len(s)):
    if t == "":   # если нет текущей строки то начинаем новую
        t = s[i]
    elif t[-1] < s[i]:
        t += s[i] # если текущий элемент больше последнего элемента текущей строки, то добавляем его в конец строки
    else:
        t = s[i] # если текущий элемент меньше последнего элемента текущей строки, то начинаем новую строку с текущим элементом
    if len(t) > maxlen:
        maxlen = len(t)
        maxstroka = t
        index_prime_sumvola = i - len(t) + 1 + 1
print(maxlen)
print(maxstroka)
print(index_prime_sumvola)

s1 = s[0]
for i in range(1, len(s)):
    if s[i-1] >= s[i]:
        s1 += " " + s[i]
    else:
        s1 += s[i]
maxlen = max([len(x) for x in s1.split()])
m = [x for x in s1.split() if len(x) == maxlen]
print(m)
print(s.index(m[0])+1)