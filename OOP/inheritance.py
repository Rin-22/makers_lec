# DRY - Don't Repeat Yourself
""" Наследование - процесс, когда один класс происходит от другого класса """

# class Parent: # родительский(базовый) класс, base
#     pass


# class Child(Parent): # дочерний(производный) класс, child, inherited
#     pass


# class Parent:
#     hands = 2
#     eyes = 2

#     def draw(self):
#         print('Родитель хорошо рисует')


# class Child(Parent):
#     pass


# ch = Child()
# ch.draw()

""" При наследовании дочерние классы перенимают все атрибуты и методы родительского класса """


# class Animal:
#     def sound(self):
#         print('Животное издает звук')

    
#     def run(self):
#         print('Животное бежит')


# class Cat(Animal):
#     def sound(self):
#         print('Мяу')

#         """ Переопределение метода - полное изменение поведения метода """


# class Dog(Animal):
#     def run(self):
#         super().run() # дополнение метода
#         print('Собака бежит')

#         """ super() - функция для обращения к родительскому классу """


# cat = Cat()
# dog = Dog()
# cat.sound()
# dog.run()



# class A:
#     attr1 = 10

#     def mul(self):
#         return self.attr1 * 2


# class B(A):
#     attr2 = 10

#     def mul(self):
#         par = super().mul()
#         return par + self.attr2


# obj = B()
# print(obj.mul()) # 30


""" Наследоваться можно от встроенных классов """

# class MyStr(str):
#     def first(self):
#         return self[0]

#     def last(self):
#         return self[-1]

#     def upper(self):
#         print('Переведено в верхний регистр')
#         return super().upper()

#     print(locals())


# str1 = MyStr('hello')
# str1.first() # h
# str1.last() # o
# str1.upper() # HELLO


# print(issubclass(MyStr, str)) # True



# class Person(object):
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age


# class Student(Person):
#     def __init__(self, name, last_name, age, course, faculty):
#         super().__init__(name, last_name, age)
#         self.course = course
#         self.faculty = faculty


# p = Person('Malik', 'Davletov', 24)
# print(dir(p))


# object -> Person -> Student


""" множественное наследование """
class A:
    def method2(self):
        print('метод А')


class B:
    def method2(self):
        print('метод В')


class C(A, B):
    pass


obj = C()
obj.method2()