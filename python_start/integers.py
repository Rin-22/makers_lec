# int()
# float()

num1 = 15
num2 = 3

""" Математические операторы """

num1 + num2 # - cложение
num1 - num2 # - вычитание
num1 * num2 # - умножение
num1 / num2 # - деление -> float()
num1 ** num2 # - возведение в степень
num1 // num2 # - деление без остатка -> int()
num1 % num2 # - выделение остатка от деления -> int


from decimal import Decimal
decimal1 = Decimal('0.1')
decimal2 = Decimal('0.1')
decimal3 = Decimal('0.1')
# print(decimal1 + decimal2 + decimal3)


""" Функции """
abs(-5) # 5
abs(4) # 4
abs(-2.5) # 2.5
# abs(x) - возвращает модуль переданного числа/число без учета знака

pow(2, 3) # 2 ** 3 = 8
pow(2, 3, 4) # 2 ** 3 % 4 = 0
# pow(x, y, [z])


divmod(1, 2) # 1 // 2, 1 % 2 - (0, 1)
# divmod(x, y)


round(2.3) # 2
round(2.6) # 3
round(2.5) # 2 - округление в меньшую сторону
round(2.3456, 2) # 2.35
# round(x, [y]) - округление переданного числа до целого, если указан 'y', то округление до 'y' знаков после запятой


# import math # библиотека для математических расчетов

# math.sqrt(25) # 5
# math.factorial(5) # 120
# # 1 * 2 * 3 * 4 * 5 - факториал числа 5
# print(math.pi)
# round(math.pi)

# num1 = float(input('Введите первое число '))
# num2 = float(input('Введите второе число '))
# print('Результат ', num1 + num2)


# x = 1
# x + 1
# print(x) # 1

# x = 2
# x = x + 1
# print(x) # 3

# x = 3
# x += 1 # x = x + 1
# print(x) # 4