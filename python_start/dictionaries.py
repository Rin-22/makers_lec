# # привет - hello

# """ словари (dict) """
# # Словарь - изменяемый, итерируемый. Состоят из пар: ключ: значение. Ключами могут быть только неизменяемые типы данных(tuple, str, int, None, bool), а значениями - любые. Ключи должны быть уникальными

# dict_ = {}
# # passport = {'name': 'Айбек', 'last_name': 'Абдулаев', 'age': 23, 'gender': 'M', 'birthday': '13.06.1997'}

# # print(passport['name']) # 'Айбек'
# # print(passport['age']) # 23
# # print(passport[0]) # KeyError

# dict2 = dict(name='Барсбек', last_name='Михаилов', age=19)
# print(dict2) # {'name': 'Барсбек', 'last_name': 'Михаилов', 'age': 19}

# dict3 = dict.fromkeys(['a', 'b'], 25)
# print(dict3) # {'a': 25, 'b': 25}

# dict4 = dict.fromkeys(['a', 'b'])
# print(dict4) # {'a': None, 'b': None}

# dict5 = dict([('name', 'John'), ('last_name', 'Watson')])
# print(dict5)
# print(dict5['name'])

""" Методы словарей """
passport = {'name': 'Айбек', 'last_name': 'Абдулаев', 'age': 23, 'gender': 'M', 'birthday': '13.06.1997'}

# passport['name'] # "Айбек"
# passport['ID'] # KeyError

# print(passport.get('name')) # "Айбек"
# print(passport.get('ID')) # None

# dict.get(key, None) - отдает значение указанного ключа, если нет - отдает второе указанное значение(по умолчанию None)

# print(passport.get('ID', 'Нет такого ключа!')) # 'Нет такого ключа!'


# passport.setdefault(key, default) - отдает значение указанного ключа, если его нет - создает его со значением default(по умолчанию - None)

# print(passport.setdefault('age')) # 23
# print(passport.setdefault('ID')) # None
# print(passport.setdefault('ID', 5234524))
# print(passport)


# passport.update({key: value}) - принимает в себя другой словарь и обновляет исходный словарь за счет него

# dict8 = {'name': 'Майрам', 'age': 27, 'name': 'Азамат', 'name': 'Кайрат', 'ID': 43781623}
# passport.update(dict8)
# print(passport)
# print(dict8)


# a = {'a': 10, 'b': 20}
# a['c'] = 30
# a['b'] = 40
# print(a) # {'a': 10, 'b': 40, 'c': 30}


dict10 = {'name': 'Алия', 'last_name': 'Азизова', 'age': 21}
# dict10.pop('name')
# print(dict10)

# deleted_el = dict10.pop('ID', 'Нет такого ключа!')
# print(deleted_el) # 'Нет такого ключа!'
# print(dict10)

# deleted_el = dict10.popitem()
# print(deleted_el)
# print(dict10)

# dict10.clear()
# print(dict10) # {}

# del dict10['age']
# print(dict10)



iter_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# for i in iter_dict:
#     print(i) # keys

# for i in iter_dict:
#     print(iter_dict[i]) # values


""" keys(), values(), items() """
k = iter_dict.keys()
# print(k)
# for key in k:
#     print(key)

v = iter_dict.values()
# print(v)
# for value in v:
#     print(value)

it = iter_dict.items()
# print(it)
# for key, value in it:
#     print(f'ключи {key}, значения {value}')


# contacts = {
#     'names': {
#         'Aidar': 'asdfasdf',
#         'Baatai': 9967357223,
#         'Igor': 99635272839
#     }
# }
# # print(contacts['names']['Igor'])
# names = contacts['names']
# print(names['Igor'])

# copy() - копирует словарь
# contacts_copy = contacts.copy()


# a1 = {'a': 1, 'b': 2, 'a': 12, 'a': 9876}
# b2 = {'c': 3, 'd': 4}
# a1.update({'c': 3, 'd': 4})
# a1.update(a=5678)
# a1.setdefault('a', 564)
# print(a1)
# a1['a'] = 22
# print(a1['a'])