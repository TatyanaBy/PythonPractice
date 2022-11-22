   
# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# Решение 1:
list=[int(a) for a in input('Введите числа через пробел: ').split()]
print(list)
list_length=len(list)
sum=0
for i in range(list_length):
      if i%2 != 0: sum = sum + list[i]
print(f'Cумма элементов на нечетных позициях равна: {sum}')

# с помощью лямбды:

from functools import reduce
# import random
# random_list= [random.randint(1,10) for i in range(random.randint(10,20))]
# print(random_list)
list1=[i for i in range(1,20)]
print(list1)
new_list = []
count = 0
for i in list1:
    if count % 2 == 1:
        new_list.append(i)
    count += 1
print(new_list)
summa = reduce((lambda x, y: x + y), new_list)
print(summa)


# Задача 2. Реализуйте алгоритм перемешивания списка.
# 1 вариант:

list1 = [1,2,3,4,5]
for i in range(len(list1)): 
    if i < len(list1):
       i+=1
print(list1)
list2 = list(reversed(list1))
print(list2)

# 2 вариант (list comprehension)

list1=[x for x in range(1,6)]
print(list1)
list2=list(reversed(list1))
print(list2)

