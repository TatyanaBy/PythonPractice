# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# работает только с целом числом
number = int (input ("Введите число: ")) 
sum = 0 
while number != 0: 
      sum = sum + number % 10 
      number = number // 10 
print (sum)

# в случае с вещественным 
number = (input ("Введите число: ")) 
sum = 0 
for a in number:
    if a.isdigit():
        sum += int(a)
print(sum)



# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


n = 4
result=1
i=1
for i in range(n):
    if i <=n:
       i += 1
       result *= i
       print(result, end= ' ')       


# Задача 3. Задайте список из n чисел последовательности (1+1/n)n и выведите на экран их сумму
#  Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} 
# Сумма 9.06


print(f'Введите n: ')
n=int(input('Введите n: '))
d={a: (1+1/a)**a for a in range(1,n+1)}
print(d)
values = d.values()
result = sum(values)
print(f'Cумма значений равна: {result}')


# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# не решено.


# Задача 5. Реализуйте алгоритм перемешивания списка.
# 1 вариант:

list1 = [1,2,3,4,5]
for i in range(len(list1)): 
    if i < len(list1):
       i+=1
print(list1)
list2 = list(reversed(list1))
print(list2)

# 2 вариант:
import random
n = int(input('Введите n: '))
list1 = []
for i in range(n):
    list1.append(random.randint(-10,100))
print(list1)   
list2 = list(reversed(list1))
print(list2)
