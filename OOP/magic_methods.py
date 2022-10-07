""" Магические методы (дандер методы - double underscore methods) """

# __init__() - инициализация объекта
# a = []
# __new__ - конструктор, отвечает за создание объектов

# class MagicClass:
#     def __new__(cls, *args, **kwargs):
#         print('сработал метод __new__')
#         return super().__new__(cls)

#     def __init__(self):
#         print('сработал метод __init__')
#         self.a = 10

# obj = MagicClass()

# Синглтон - паттерн, подразумевающий наличие только 1 объекта

# class Contact:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             return cls._instance
#         raise Exception('Объект уже создан!')
    
#     def __init__(self, phone, name) -> None:
#         self.phone = phone
#         self.name = name

# c1 = Contact('996555888999', 'Georgiy')
# c2 = Contact('996252526264', 'Akakiy')


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self):
        # человеко читабельное отображение
        return self.name

    def __repr__(self):
        # отображение для компьютера
        return self.name

    def __del__(self):
        # деструктор
        print('Объект удален')
        del self

    """  
    Перегрузка операторов сравнения
    __gt__ - >
    __lt__ - <
    __eq__ - ==
    __ne__ - !=
    __ge__ - >=
    __le__ - <=
    """
    def __gt__(self, other):
        return self.age > other.age

    """  
    Перегрузка математических операторов
    __add__ - +
    __sub__ - -
    __mul__ - *
    __truediv__ - /
    __floordiv__ - //
    __pow__ - **
    __mod__ - %
    """
    def __add__(self, other):
        return self.age + other.age

    """  
    Операции на атрибутами
    __setattr__
    __getattr__
    __delattr__
    __getattribute__
    """
    def __getattr__(self, name):
        print('Получаем объект')
        return self.__dict__.get(name)

    def __getattribute__(self, __name: str):
        print('сработал __getattribute__')
        return super().__getattribute__(__name)


# a = Person('Valentin', 25)
# b = Person('Vitaliy', 23)
# print(a.last_name) # - __getattr__
# print(a.age)
# a.rating = 100 # __setattr__
# del a.rating # __delattr__
# print(a > b)
# print(a.__gt__(b))
# print(a + b)
# print(a)
# list_ = []
# list_.append(a)
# print(list_)


class MyDict(dict):
    """  
    __len__(self)
    __getitem__(self, key)
    __setitem__(self, key, value) - self[key] = value
    __delitem__(self, key) - del self[key]
    __contains__(self, item) - item in self
    """
    def __getitem__(self, key):
        print('__getitem__')
        return super().__getitem__(key)
    
    def __setitem__(self, key, value):
        print('__setitem__')
        super().__setitem__(key, value)

# obj = MyDict(a=5, b=6, c=7)
# print(obj['a'])
# obj['d'] = 10
# print(obj)

class Human:
    def __init__(self, name) -> None:
        self.name = name

    def __len__(self):
        counter = 0
        for i in self.name:
            counter += 1
        return counter

    def __contains__(self, item):
        # for i in self.name:
        #     if i == item:
        #         return True
        # else:
        #     return False
        return any(i for i in self.name if i == item)
        
    
# h = Human('Vasiliy')
# print(len(h))
# print('a' in h)

""" __iter__ и __next__ """

# str_ = 'hello'
# for i in str_:
#     print(i)
# a = str_.__iter__()
# print(a)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__()) # StopIteration

# list_ = [1, 2, 3, 4, 5]
# l = iter(list_)
# while True:
#     try:
#         res = next(l)
#         print(res)
#     except StopIteration:
#         break

