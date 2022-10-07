""" Встроенные функции """

# print()

# Приведение к определенному типу
# int()
# str()
# dict()
# list()
# set()
# tuple()
# bool()
# complex()
# float()


# pow()
# divmod()


# dir() - возвращает список атрибутов и методов переданного объекта
# type()
# id()
# a = 10
# print(isinstance(a, int))

# len()
# min()
# max()
# sum()


""" 
map, filter, enumerate, zip, reduce

lambda
"""

# map(func, iterable) - принимает функцию и какой-то итерируемый объект. Применяет переданную функцию к каждому элементу итер. объекта


# def func1(num):
#     return num + 10

# nums = [1, 2, 3, 4, 5]

# res = list(map(func1, nums))
# res2 = [num + 10 for num in nums]

# print(res)
# print(res2)


# def func1(list1, list2):
#     return list1 + list2

# nums = [1, 2, 3, 4, 5]
# nums2 = [1, 2, 3, 4, 5, 6]

# res = list(map(func1, nums, nums2))

# print(res)


# words = ['apple', 'map', 'laptop']

# def func2(word):
#     return word + '15'

# res = map(lambda word: word + '15', words)
# res2 = map(func2, words)
# print(list(res))
# print(list(res2))

# lambda param: тело функции - lambda - анонимная функция, которая живет только на момент ее выполнения


# filter(func, iterable) - принимает функцию(-> bool) и итер объект. Фильтрует по условию указанному в функции

# nums = [76, 89, 35, 65, 43, 85]
# def filter_num(num):
#     return num % 5 == 0

# res = filter(filter_num, nums)
# res2 = list(filter(lambda num: num % 5 == 0, nums))
# res3 = [num for num in nums if num % 5 == 0]

# print(list(res))
# print(res2)
# print(res3)


from functools import reduce

# reduce(func, iterable) - принимает функцию, итер объект. Сводит все элементы итер объекта в одно значение

# nums = [10, 20, 30, 40]
# def func3(num1, num2):
#     return num1 + num2

# res = reduce(func3, nums)
# res2 = reduce(lambda num1, num2: num1 + num2, nums)
# print(res)
# print(sum(nums))
# print(res2)
# nums = [10, 20, 30, 40]
# min_value = reduce(lambda x, y: x if x < y else y, nums)
# # x = 10, y = 20 -> x = 10, y = 30 -> x = 10, y = 40
# print(min_value)
# print(min(nums))


# enumerate(iterable) - принимает последовательность элементов, и нумерует каждый элемент последовательности

# a = 'word'
# res = enumerate(a)
# print(list(res))
# print(dict(res))

# b = ['h', 'e', 'l', 'l', 'o']
# res2 = enumerate(b, start=12)
# # print(tuple(res2))
# for i in res2:
#     print(i)


# a = 'world'
# b = iter(a)
# while True:
#     try:
#         print(b.__next__())
#     except StopIteration:
#         break


# zip() - связывает элементы переданных последовательностей

# list1 = [1, 2, 3]
# list2 = {'a': 1, 'b': 2, 'c': 3}
# list3 = ['Masha', 'Dasha', 'Pasha']
# zipped_list = list(zip(list1, list2, list3))
# lista, listb, listc = zipped_list
# print(lista)
# print(listb)
# print(listc)
# print(zipped_list)


""" all(), any() """

# all(iterable) - возвращает True, если ВСЕ элементы внутри последовательности являются True, иначе False

# list_ = [True, True, True]
# print(all(list_)) # True

# list_1 = [True, False, True]
# print(all(list_1)) # False

# nums = [9, 7, 1, 5, 6]
# print(all(nums)) # True

# nums2 = [9, 7, 0, 5, 6]
# print(all(nums2)) # False

# 0
# False
# None
# ''
# {}
# []
# set()
# tuple()

# all('hello') # True
# all((1, 2, 3)) # True
# all(map(lambda x: x + 10, [1, 2, 3])) # True
# all(i for i in range(10)) # False

# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     else:
#         return True


# any(iterable) - возвращает True, если ХОТЯ БЫ ОДИН элемент в последовательности True, иначе False


# list_ = [True, True, True]
# print(any(list_)) # True

# list_2 = [False, True, False]
# print(any(list_2)) # True

# nums = ['', [], tuple(), set(), {}, False, None, 10]
# print(any(nums)) # True

# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False

# password1 = 'mysuperpassworD10$'
# spec_symb = '@#%?$'
# def check_password(password):
#     if not any(i.isupper() for i in password):
#         raise ValueError('Пароль должен содержать хотя бы 1 символ верхнего регистра')
#     if not any(i.isdigit() for i in password):
#         raise ValueError('Пароль должен содержать хотя бы одну цифру')
#     if not any(i for i in password if i in spec_symb):
#         raise ValueError('Пароль должен содержать хотя бы один спец символ')
#     return password
    
# check_password(password1)



# callable(obj) - принимает объект и проверяет можно ли его вызвать

# def func(x):
#     return x


# print(callable(func)) # True
# func(10)

# a = 'string'
# print(callable(a)) # False


# def func2(x, y):
#     return x / y

# func2(10, 5)

# func3 = lambda x, y: x / y
# callable(func3) # True
# func3(20, 2)



# eval() - принимает какое-то утверждение и выполняет его

# eval('print(10)')

# num1 = int(input('1 '))
# num2 = int(input('2 '))
# operator = input('op ')
# eval(f'print({num1}{operator}{num2})')


# exec() - выполняет блоки кода
# a = """  
# for i in range(1, 10):
#     print(i)
# """
# exec(a)







# res = map(lambda x: x * 2, range(1, 10))
# print(set(res))
# print(list(res))

# def func(x):
#     return x

# def gen_func(x):
#     for i in range(x):
#         yield i

# res = gen_func(8)
# print(list(res))
# print(set(res))

# print(list(gen_func(10)))
# print(set(gen_func(10))) 
