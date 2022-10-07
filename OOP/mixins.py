""" Миксины """

# Mixin - классы, которые используются для дополнения функционала других путем наследования. От миксинов нельзя создавать объекты

# class MicrowaveMixin:
#     def heat(self):
#         print('грею еду')


# class Fridge:
#     def cold(self):
#         print('охлаждаю еду')


# class TV:
#     def watch_tv(self):
#         print('передаю шоу')


# class Cooker:
#     def cook(self):
#         print('готовлю еду')


# class Kitchen(MicrowaveMixin, TV, Cooker, Fridge):
#     p = 10



class BaseClass:
    def eat(self):
        pass


class BaseMixin:
    def eat(self):
        print('я много ем')


class ChildrenClass(BaseMixin, BaseClass):
    pass


obj = ChildrenClass()
obj.eat()

# При наследовании от миксинов и других классов - миксины нужно указывать в первую очередь (MRO)
