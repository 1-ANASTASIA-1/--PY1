list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел
unic = set(list_)
summa = sum(unic)
kolvo = len(unic)
av = round(summa/kolvo,5)
print(summa)
print(kolvo)
print(av)