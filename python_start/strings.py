""" Cтроки (string) """

# str() 

# Строки - неизменяемый, упорядоченный, индексируемый тип данных

string = "Hello"

string2 = 'Hello'

doc_string = """ Обычно используется для написания документации
к коду """
doc_string2 = ''' Обычно используется для
написания документации в несколько строк '''

string3 = "Hello, I'm student"

string4 = 'Hello, I\'m teacher'


str1 = 'Hello'
str2 = 'World'
# print(str1 + str2)
# Конкатенация - склеивание строк/сложение строк

# str3 = 'Quak'
# num1 = 3
# print(str3 * num1)


""" Функции и методы строк """
my_str = 'hello world'

# print(len(my_str)) # - выводит длину строки
# print(my_str.split(separator)) # - делит по указанному делителю (по умолчанию - пробел)
my_str.replace('l', 'b') # hebbo worbd - замена подстроки в строке
my_str.upper() # HELLO WORLD - перевод в верхний регистр
my_str.lower() # hello world - перевод в нижний регистр
my_str.title() # Hello World - перевод первого символа каждого слова в верхний регистр
my_str.capitalize() # Hello world - перевод первого символа строки в верхний регистр
'ß'.casefold() # 'ß' - ss - эсцет - более агрессивный перевод в нижний регистр
my_str.count('l') # 3 - считает количество вхождений переданной подстроки

""" Индексы и срезы """
# str7 = 'hello world'
# Индекс - порядковый номер символа в строке(начиная с 0)
# 'makers'
#  012345
# -054321
# print(str7[4])
# print(str7[10])
# print(str7[len(str7)-1])
# print(str7[-1])

# str7 = 'hello world'

# print(str7[0:5]) # hello
# str7[start:stop]

# print(str7[4:]) # от старта до конца строки
# print(str7[:7]) # от начала до указанного индекса
# print(str7[0:-1:2]) # str7[start:stop:step]
# print(str7[::-1]) # отрицательный шаг начинает чтение строки с конца

str7 = 'hello world'
# print(str7.find('2')) # 1 - поиск индекса подстроки в строке
# print(str7.index('2')) # - ValueError
# print('*'.join(['hello', 'world', 'bye'])) # соединяет переданный список строк по указанной строке
str8 = '   my name is akbar    '
# print(str8)
# print(str8.strip(symbol)) # убирает указанный символ в строке с двух сторон, если не указан символ, по умолчанию - пробел
# str8.lstrip() # - убирает пробелы слева
# str8.rstrip() # - убирает пробелы справа

# print(str8.isalpha())


string = 'My test string 123'
# print(string.isdigit())
string.isalpha() # False
string.isalnum() # False
string.isspace() # False
string.islower() 
string.isupper()
string.endswith('123')
string.startswith('My')


num1 = 10
num2 = 20
num1 > num2 # False
num1 < num2 # True
num1 == num2 # False
num1 != num2 # True - неравенство
num1 <= num2 # True
num1 >= num2 # False


# str1 = 'apple'
# str2 = 'abple'
# print(str1 > str2)
# ord('a') # 97
# chr(97) # 'a'
# ASCII

# a = 'abcde'
# b = 'abced'
# print(sorted(a))
# print(sorted(b))


""" Форматирование/интерполяция строк """

stat = 'Привет, Фархад! Приглашаю тебя на праздник!'

# name = input()
# place = input()
# %
# str5 = 'Привет, %s!' % name
# print(str5)
# str6 = 'Привет, {}! Приглашаю тебя на {}'.format(place, name)
# print(str6)
# str7 = f'Hello {name}! Welcome to {place}'
# print(str7)


# Форматирование строк - подстановка переменных в строку, создание динамической строки

""" Экранирование строк """

# a = 'I\'m student'
# b = 'Идет бычок качается,\n\tВздыхает на ходу'
# print(b)
# # \n - newline
# # \t - tabular

# str8 = r'This is test string\n\t\n'
# print(str8)
# raw

# windows_path = 'Users\Documents\\new_folder'
# print(windows_path)

# string = 'Hello world'
# string2 = 'ell'
# print(string2 in string)

# dir(obj) - функция возвращает список методов доступных переданному объекту
# str1 = 'hello'
# print(dir(str1))
