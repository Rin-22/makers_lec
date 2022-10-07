"""  
ООП - объектно ориентированное программирование
"""
# класс 
    # методы
    # атрибуты

# объекты

"""  
Наследование
Полифорфизм
Инкапсуляция

Абстракция
Ассоциация (Композиция, Агрегация)
"""
# Наследование - DRY - Множественное наследование 
# class Mom:
#     pass

# class Dad:
#     pass

# class Child(Mom, Dad):
#     pass

# # Child.__init__()
# print(Child.mro())

# Инкапсуляция
# защита данных
# объединение методов в один класс
# Модификаторы доступа
# public - везде
# _protected - в классе и в дочерних
# __private - только в классе (_ClassName__private)

# Интерфейс (setter|getter)
# @property
class D:
    __p = 10

    @property
    def p(self):
        return self.__p

    @p.setter
    def p(self, value):
        self.__p = value

    """  
    instance - self - ко всему
    classmethod - cls - только к атрибутам класса
    staticmethod - () - ни к чему
    """
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        cls.obj = 20
        return super().__new__(cls)

    def __init__(self, age) -> None:
        self.name = self.concatenate('Pasha')
        self.age = age

    @classmethod
    def change_cls_value(cls):
        cls.obj = 50

    @staticmethod
    def concatenate(data):
        return data + 'OV'

a = D(age=10)
# # a.get_p() # 10
# # a.get_p # 10
# a.p # 10
# a.p = 30
# a.obj # 20
# a.change_cls_value()
# a.obj # 50


