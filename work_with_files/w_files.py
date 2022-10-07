""" Работа с файлами """

# Операции над файлами:
# 1. Чтение
# 2. Запись

# Файлы бывают текстовыми и бинарными

# open(путь_до_файла, режим_работы) - функция для открытия файлов

# file = open('test.txt', 'r')
# print(file.read())
# file.close()

"""  
r - чтение
w - запись, создает файл, перезаписывает содержимое файла, если такой файл существует
x - запись, если файла не существует, иначе исключение
a - дозапись
w+, r+ - запись и чтение
b - открытие бинарных файлов
t - открытие текстовых файлов
rt - режим по умолчанию
"""

# file = open('test.txt', 'r')
# print(file.read(6))
# file.close()

# read(n) - читает весь файл или n символов, если указан

# file1 = open('test.txt')
# for row in file1:
#     print(row)
# file1.close()

# file2 = open('test.txt')
# words = file2.readlines()
# list_ = []
# for word in words:
#     list_.append(word.strip())
# print(list_)
# file2.close()

# readlines() - читает файл и возвращает список из строк

# image = open('banana1.jpeg', 'rb')
# print(image.read())
# image.close()


# file5 = open('test2.txt', 'r')
# print(file5.read())
# file5.seek(0)
# print(file5.read())
# print(file5.tell())
# file5.close()

# seek(n) - перенос курсора на n позицию
# tell() - сообщает положение курсора


# with open('test2.txt', 'r') as file10:
#     a = 10
#     print(file10.read())


# print(a)

# with функция() as название: - контекстный менеджер
#     тело менеджера

# try:
#     file10.read()
#     file10.seek(0)
# finally:
#     file10.close()


# with open('test2.txt', 'r') as file1:
#     print(file1.readlines())


# file1.read()



# with open('test3.txt', 'w') as f:
#     f.write('apple\n')
#     f.write('banana\n')
#     f.write('pear\n')
#     f.write('tomato\n')

# with open('test4.txt', 'w+') as f:
#     list_ = ['Masha', 'Oleg', 'Pavel', 'Sergey']
#     n = [name + '\n' for name in list_]
#     f.writelines(n)
#     f.seek(0)
#     print(f.read())


# with open('prog.txt', 'w+') as f:
#     f.write('for i in range(1, 10):\n\tprint(i)')
#     f.seek(0)
#     code = f.read()
#     exec(code)


# with open('prog.txt') as f:
#     print(f.readline())
#     print(f.readline())


# with open('work_with_files/makers.txt', 'w') as file:
#     file.write('another text')


# with open('work_with_files/makers.txt', 'a') as file:
#     file.write('\nappended text')


# with open('work_with_files/bootcamp.txt', 'x') as file:
#     file.write('\nappended text')


# csv - Comma Separated Values

# import csv


# with open('students.csv', 'w') as file:
#     csv_writer = csv.writer(file, delimiter=',')
#     csv_writer.writerow(['#', 'ФИО', 'Дата рождения', 'Курс'])
#     csv_writer.writerow(['1', 'Василий Пупкин', '25.12.2004'])


# with open('students.csv', 'r') as file:
#     csv_reader = csv.reader(file, delimiter=',')
#     for row in csv_reader:
#         print(row)


