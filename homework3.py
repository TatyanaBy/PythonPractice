# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
list=[int(a) for a in input('Введите числа через пробел: ').split()]
print(list)
list_length=len(list)
sum=0
for i in range(list_length):
    if i%2 != 0:
        sum = sum + list[i]
print(f'Cумма элементов на нечетных позициях равна: {sum}')

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
list1_length=int(input('Введите длину списка: '))
list1=[]
for i in range(list1_length):
    list1.append(int(input(f'введите число{i+1}: ')))
print(list1)
list2_length=int(len(list1)/2+len(list1)%2)
list2=[]
for i in range(list2_length):
    productNumbers=list1[i]*list1[len(list1)-1-i]
    list2.append(productNumbers)
print(f'произведение пар чисел списка: {list2}')   

# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов. Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
list=[float(a) for a in input('Введите числа через пробел: ').split()]
print(list)
min = 0
max = 0
# difference=max-min
for i in list:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)  
print(f'Максимальное значение дробной части элементов: {max}')
print(f'Минимальное значение дробной части элементов: {min}')
print(f'Разница: {max - min}')



# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# # через функцию bin
a = int(input('введите число: ')) 
print(bin(a))

# # 2 вариант:
a = int(input('введите число: ')) 
a2 = '' 
while a > 0:
    a2 = str(a % 2) + a2
    a = a // 2 
print(f'Введенное число в двоичной системе исчисления равно: {a2}')



# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# что-то я тут запуталась(((

k = int(input('Введите число: '))
f1 = f2 = 1
f3 = f4 = -1
print(f3, f4, f1, f2, end=' ')
 
for i in range(2, k):
    f1, f2 = f2, f1 + f2
    f3, f4 = f2, f1 - f2
    print(f4, f2, end=' ')


