""" Полиморфизм """

# Полиморфизм - принцип ООП, который заключается в использовании одной сущности(метод, оператор) для различных типов объектов.

# +
num1 = 10
num2 = 30
print(num1 + num2) # сложение - 40

str1 = 'Hello'
str2 = 'World'
print(str1 + str2) # конкатенация - HelloWorld


# class A:
#     def method1(self):
#         return 10 + 10


# class B:
#     def method1(self):
#         return 'метод1'


# objA = A()
# objB = B()
# for obj in (objA, objB):
#     print(obj.method1())



# class Cat:
#     def meow(self):
#         print('мяу')


# class Dog:
#     def bark(self):
#         print('Гав')


# cat1 = Cat()
# dog1 = Dog()
# for animal in (cat1, dog1):
#     if type(animal) is Cat:
#         animal.meow()
#     else:
#         animal.bark()

# class Cat:
#     def sound(self):
#         print('мяу')


#     def __str__(self):
#         return 'Я кошка'
    

# class Dog:
#     def sound(self):
#         print('Гав')

    
#     def __str__(self) -> str:
#         return 'я собака'


# cat1 = Cat()
# dog1 = Dog()
# for animal in (cat1, dog1):
#     animal.sound()


# len('12341243')
# len([1, 2, 3])
# len({1: '2'})

# class MyClass:
#     def __len__(self):
#         return 10

# obj = MyClass()
# print(len(obj))


""" Абстракция """

# Абстракция - сущность без конкретной реализации


# class Animal:
#     def __init__(self) -> None:
#         self.eat()
#         self.sound()
#         self.move()

#     def eat(self):
#         raise NotImplementedError(self.__class__.__name__)

#     def sound(self):
#         raise NotImplementedError(self.__class__.__name__)

#     def move(self):
#         raise NotImplementedError(self.__class__.__name__)


# class Cow(Animal):
#     def eat(self):
#         print('я ем траву')

    
# cow = Cow()
# cow.eat()


from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def get_x(self):
        return 'x'

    
    @abstractmethod
    def abs_method(self):
        print('ыфвафыва')


class ConcreteClass(AbstractClass):
    def method1(self):
        print(12121)

    
    def abs_method(self):
        return 'Hello world'


obj = ConcreteClass()
