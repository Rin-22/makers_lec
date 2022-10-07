""" ООП - объектно ориентированное программирование """
# Классы - участки кода, которые описывают какой-то тип данных/объект. 

class MyClass:
    a = 10 # атрибут класса

# Атрибут класса - атрибут/переменная класса, которая относится ко всем созданным объектам/экземплярам от этого класса. У каждого объекта есть своя копия атрибутов

# class Human:
#     skin = True
#     hands = 2
#     head = 1


# h = Human() # объект/экземпляр класса
# # print(type(h))
# # print(h.hands)
# h.hands = 3
# print(h.hands)
# h2 = Human()
# print(h2.hands)


class Human:
    hands = 2
    head = 1
    legs = 2

    def __init__(self, age, height, weight):
        self.height = height
        self.weight = weight
        self.name = 'Vanya'
        self.age = age
        # атрибуты экземпляра класса - атрибуты присущие конкретному объекту/экземпляру


human1 = Human(25, 185, 80)
human2 = Human(height=175, age=23, weight=65)
print(human1.age)
print(human2.age)


# Метод - функция, которая определена внутри класса и описывает какое-то действие


# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         # self - ссылка на объект класса
#         print(f'{self.name} лает')


# dog1 = Dog('Tuzik')
# dog1.bark()
# Dog.bark(dog1)


# class Student:
#     course = 4


#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age

    
#     def get_info(self):
#         # Сергей Бурунов, 23
#         return f'{self.name} {self.last_name}, {self.age}'

    
#     def sleep(self):
#         print('спать во время занятий')

    
#     def write(self):
#         print('Пишу лекции')


# stud1 = Student('Vasya', 'Alekhin', 22)
# stud2 = Student('Imran', 'Bakaev', 21)
# stud1.sleep()
# print(stud2.get_info())
# stud1.write()


# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def birthday(self):
#         self.age += 1
#         return f'{self.name} теперь {self.age} лет!'


# person1 = Person('Алекс', 23)
# print(person1.age)
# print(person1.birthday())
# print(person1.age)
# person1.legs = 3
# print(person1.legs)



class Car:
    car_counter = 0

    def __init__(self, color, model):
        self.color = color
        self.model = model
        Car.car_counter += 1


    def __str__(self):
        return f'{self.color} {self.model}'


car1 = Car('red', 'Toyota')
# print(car1.car_counter)
car2 = Car('blue', 'Mercedes')
# print(car2.car_counter)
# print(car1)

# type(obj) - позволяет узнать тип объекта

# isinstance(obj, class) - возвращает True/False, если переданный объект принадлежит указанному классу

# print(isinstance(12, int))

# int
# list
# dict
# tuple
# set
# bool
# frozenset

# a = [1, 2, 3, 4]

"""  
Наследование
Инкапсуляция
Полиморфизм

Агрегация
Абстракция
Композиция
"""


# class MyClass:
#     var1 = 10

#     def __init__(self):
#         self.var2 = 20
#         self.var3 = 30


# obj = MyClass()
# obj.var1 # 10
# obj.var2 # 20
# obj.var3 # 30
# obj.var4 = 40
# print(obj.__dict__)
# setattr(obj, 'var5', 60) # obj.var5 = 60
# print(obj.var5) # 60
# print(hasattr(obj, 'var7')) # False
# print(getattr(obj, 'var1')) # obj.var1 - 10
# # print(getattr(obj, 'var10', 'Нет такого атрибута'))



# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('Объект создан')
#         # __init__ - инициализатор объектов

    
#     def __del__(self):
#         print('Объект удален')
#         # __del__ финализатор объекта

# p1 = Person('Oleg', 25)



# class Product:
#     def __init__(self, title: str = 'Товар', price: float = 0.0, quantity: int = 0, desc: str = 'Нет описания'):
#         if not isinstance(title, str):
#             raise ValueError('title must be str')
#         self.title = title
#         self.price = price
#         self.quantity = quantity
#         self.desc = desc

# a = Product(title=35374)


# from dataclasses import dataclass
# from typing import Any

# @dataclass
# class Product:
#     title: str
#     type_: Any
#     price: float = 0.0
#     quantity: int = 0
#     description: str = 'Нет описания'


# prod1 = Product(title=1234, type_='Rice', price=90.0, quantity=10)
# print(prod1.__dict__)



# class Animal:
#     pass


# a = Animal()
# a.legs = 4
# print(a.__dict__)


class Cars(object):
    __slots__ = ['model', 'color', 'brand']

    def __init__(self, model, color, brand) -> None:
        self.model = model
        self.color = color
        self.brand = brand


car1 = Cars('Toyota', 'red', 'Camry')
# car1.volume = 3.8  # AttributeError
# print(car1.__dict__)
print(dir(car1))