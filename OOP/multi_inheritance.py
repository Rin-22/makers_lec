""" Множественное наследование """

class Dad:
    eyes = 'green'
    hair = 'black'


class Mom:
    hair = 'brown'
    eyes = 'blue'


class Child(Dad, Mom):
    pass


child = Child()
# print(child.eyes) 
# print(child.hair)

""" Поиск атрибутов и методов идет слева направо """


# class.mro() - метод для получения списка порядка поиска методов и атрибутов - method resolution order

# print(Child.mro())



""" Проблема ромба """
# class A:
#     def method(self):
#         print(A.__name__)


# class B(A):
#     def method(self):
#         print(B.__name__)


# class C(A):
#     def method(self):
#         print(C.__name__)


# class D(B, C):
#     def method(self):
#         # super().method() # обращение к родителю
#         A.method(self) # делегирование
#         print('МЕТОД D')


# obj = D()
# obj.method()
# print(D.mro())


""" перекрестное наследование (не решено) """
# class A:
#     pass

# class B:
#     pass

# class C(A, B):
#     pass

# class D(B, A):
#     pass

# class E(C, D):
#     pass


# SOLID
# S - single responsibilty
# O - open-closed
# L - Liskov substitution
# I - Interface segregation
# D - Dependency inversion



# S
# class DateTemp:
#     def date(self):
#         print('сейчас 3 часа')

#     def temp(self):
#         print('сейчас 40 градусов')


# class Date(DateTemp):
#     pass


# class Temp(DateTemp):
#     pass


# class Date:
#     def time(self):
#         print('сейчас 4 часа')


# class Temp:
#     def temp(self):
#         print('сейчас 30 градусов')


# class DateTemp(Date, Temp):
#     pass
