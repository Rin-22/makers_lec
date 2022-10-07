""" Условные выражения """

# >
# <
# ==  
       # --> bool()
# !=
# >=
# <=

# print(20 > 10)
# print(13 < 5)

# print(bool(0)) # False
# print(bool(1)) # True
# print(bool(2)) # True
# print(bool(-3)) # True

bool('') # False
bool([]) # False
bool({}) # False
bool(set()) # False
bool(None) # False


""" if """
# num = 15
# if num > 16:
#     print('Hello world')

""" else """
# num = 15
# if num > 16:
#     print('Hello world')
# else:
#     print('Goodbye world')


# temperature = 40
# if temperature < 20:
#     print('холодно')
# else:
#     if temperature < 30:
#         print('тепло')
#     else:
#         if temperature > 35:
#             print('жарко')

""" elif """
# temperature = 40
# if temperature < 20:
#     print('холодно')
# elif temperature < 30:
#     print('тепло')
# elif temperature < 35:
#     print('жарко')
# else:
#     print('очень жарко')


# num = 15
# if num < 20:
#     print('ok')
# if num > 10:
#     print('same')
# if num < 23:
#     print('good')


# mark = int(input('Введите оценку от 1 до 10 '))

# if mark == 10:
#     result = 5
# elif mark < 3:
#     result = 2
# elif mark < 5:
#     result = 3
# else:
#     result = 4
# print(result)

# if условие:
#     действие
# elif условие:
#     другое_действие
# else:
#     действие в случае если ни одно из выше указанных условий не сработало

# s = 'hello'
# s.isalnum()
# s.isalpha()
# s.isdigit()

# in - проверка на вхождение
# string = 'Привет! Как твои дела?'
# if 'привет' in string.lower():
#     print('со мной поздоровались :)')
# else:
#     print(';-(')


# string = 'Привет! Как твои дела?'
# if 'привет' not in string.lower():
#     print(';-(')
# else:
#     print('со мной поздоровались :)')


""" and, or, not """
False and False # False
True and True # True
False and True # False
True and False # False

# age = 19
# if age > 15 and age < 18:
#     print('Ok')
# else:
#     print('Not ok')


False or True # True
True or False # True
False or False # False
True or True # True

# age = 19
# if age > 15 or age < 18:
#     print('Ok')
# else:
#     print('Not ok')


not False # True
not True # False


# print(int(False)) # 0 
# print(int(True)) # 1
True + True # 2

# a = 10
# [действие1, действие2][условие]
# print(['ok', 'not ok'][a > 5])


""" Тернарный оператор """
# a = ''
# msg = input('Введите сообщение ')
# if len(msg) > 10:
#        a = 'Сообщение длиннее 10 символов'
# else:
#        a = 'Сообщение меньше 10 символов'
# print(a)

# msg = input('Введите сообщение ')
# a = 'Сообщение длиннее 10 символов' if len(msg) > 10 else 'Сообщение меньше 10 символов'
# print(a)
# действие if условие else другое_действие


# a = 1
# if a:
#        print('ok')


# color = input('выберите цвет ')
# match color:
#        case 'red':
#               print('ok, red')
#        case 'white':
#               print('ok, white')
#        case 'black':
#               print('ok, black')
#        case _:
#               print('we don\'t have this color')



# a = 'string'
# assert len(a) == 0
# print('It\'s ok')

# first_num = int(input('1 '))
# assert first_num == 30, 'число не верное'
# print('число верное!')