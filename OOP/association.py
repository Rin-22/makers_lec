""" ассоциация (агрегация, композиция) """


""" агрегация """
# class Battery:
#     def __init__(self) -> None:
#         self.power = 100

# class Electronic:
#     def __init__(self, model, color) -> None:
#         self.model = model
#         self.color = color
#         self.battery = Battery()

# class Phone(Electronic):
#     pass

# class Laptop(Electronic):
#     pass


# phone = Phone('Samsung', 'black')
# phone.battery.power # 100
# bat = Battery()

""" композиция """
# class Human:
#     class Heart:
#         def __init__(self) -> None:
#             self.heart = '4-хкамерное'

#     class Kidneys:
#         def __init__(self, q) -> None:
#             self.q = q

#     class Eyes:
#         def __init__(self, color):
#             self.color = color

#     def __init__(self, q, color) -> None:
#         self.heart = self.Heart()
#         self.kidneys = self.Kidneys(q)
#         self.eyes = self.Eyes(color)


# h = Human(2, 'blue')
# e = Human.Eyes('green')
        

