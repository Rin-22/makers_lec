""" Функции """

# print()
# max()
# pow()

# функция - именнованный блок кода, который принимает какие-либо значения, совершает над ними определенные действия и возвращает результат этих действий

# a1 = 100
# (a1 ** 2) / 10 * 15
# a2 = 200
# (a2 ** 2) / 10 * 15
# a3 = 400
# (a3 ** 2) / 10 * 15

# DRY(Don't Repeat Yourself) - не повторяйся


# def func():
#     print('Hello world')

# func()


# def my_sqr(num):
#     print((num ** 2) / 10 * 15)


# a = my_sqr(100) # None
# a + 500 # TypeError


# def my_func(num):
#     return (num ** 2) / 10 * 15


# b = my_func(100) # 15000.0
# print(b)
# print(b + 500)


# a = print()
# print(a)


# def func():
#     return None


# def имя_функции(параметры):
#     тело_функции

# имя_функции(аргументы)

# параметры - это значения функции при объявлении

# аргументы - это значения для функции при вызове

# return - ключевое слово для возвращения результата выполнения функции


# def add(x: int, y: int) -> int:
#     """ Принимает 2 числа и складывает их между собой """ # строка документации (docstring)
#     num = x + y
#     return num

# print(add(10, 15))
# print(add('asdf', 'dfkasdf'))


# параметры бывают 2 типов:
# 1. обязательные (с)
# 2. необязательные(по умолчанию) (с=10)

# def sub(x, y):
#     res = x - y
#     return res

# a = sub(25, 10) # 15
# print(a)

# def sub1(x, y=5):
#     res = x - y
#     return res

# b = sub1(10) # 5
# c = sub1(50, 10) # 40
# print(b)


# def func(x=5, y): # SyntaxError

# def func(a, b, c, d, e=10, f=20):
#     pass # Ok


# аргументы бывают:
# 1. именнованные
# 2. позиционные

def my_func(num1, num2, num3=10):
    return num1 + num2 + num3

# позиционные
# my_func(10, 25, 30) # 65
# my_func(50, 60) # 120

# именнованные
# my_func(num1=5, num2=10, num3=15)
# my_func(num3=10, num1=5, num2=7)

# my_func(10, 5, num3=10) # 25
# my_func(num3=5, 5, 10) # Error
# my_func(10, 5, num1=15) # Error


# def send_message(email, message):
#     return f'{message} было отправлено на {email}'


# def notify_user(name):
#     message = input('Введите сообщение ')
#     email = input('Введите почту ')
#     note = send_message(email, message)
#     print(f'Здравствуйте {name}. {note}')


# notify_user('Актан')


# print(1, 2, 3,4 , 45, 454, 556, 6, 66, 7)
# print()


# *args - кортеж позиционных аргументов (arguments)
# **kwargs - словарь именнованных аргументов (keyword arguments)


# def func(*args, **kwargs):
#     print(args, 'args')
#     print(kwargs, 'kwargs')


# func(1, 2, 3, 4) # args -> (1, 2, 3, 4)
# func(a=1, b=2, c=3, d=4) # kwargs -> {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# func(1, 2, 3, a=10, b=15, c=16)
# func()


# def my_func(*args):
#     counter = 0
#     for i in args:
#         try:
#             counter += i
#         except TypeError:
#             print(f'{i} не является числом')
#     return counter


# print(my_func(1, 2, 3, 4, 'fghjk', 6))
