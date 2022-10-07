""" JSON """

# JavaScript Object Notation

# human = {
#     'name': 'Aleksey',
#     'age': 50,
#     'is_married': True,
#     'hobbies': ['music', 'football', 'games'],
#     'job': None
# }

# import json

# JSON - формат обмена данными между языками, основанный на JavaScript

# Сериализация - перевод питон-объектов в JSON-объекты

# json_str = json.dumps(human)
# print(json_str)


# Десериализация - перевод json-объекты в python-объекты

# json_human = '{"name": "Turar", "last_name": "Akimov", "job": null, "is_married": false}'
# python_human = json.loads(json_human)
# print(python_human)

# p = [
#     {
#         'title': 'Apple Iphone 13',
#         'price': 37378
#     },
#     {
#         'title': 'Samsung Galaxy S21',
#         'price': 10000
#     },
#     {
#         'title': 'Nokia 3310',
#         'price': 123451
#     }
# ]


# with open('products.json', 'w+') as file:
#     products = json.dumps(p)
#     file.write(products)
#     file.seek(0)
#     python_products = json.load(file)
#     print(python_products)


# file = open('products2.json', 'w')
# json.dump(p, file, indent=4)
# file.close()
# print(file.closed)

