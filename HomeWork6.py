# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def Method(a, b):

#   if b > 0: return a*Method(a, b - 1);
#   else: 
#     if b < 0: return (1/a)*Method(a, b + 1);
#     else: return 1;


# print(Method(3, 5))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

# def sum(a, b):
#     if a == 0:
#         return b
#     else:
#         return sum(a - 1, b + 1)


# print(sum(2, 2))