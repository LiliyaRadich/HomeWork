# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

num = int(input('введите кол-во элементов списка: '))
work_list = [random.randint(0, 10) for i in range(num)]
print(work_list)
find_dig = int(input('введите значение, которое нужно найти в списке: : '))
count = 0
for dig in work_list:
    if dig == find_dig:
        count += 1
print(f'Число {find_dig} встречается в списке {count} раз')
