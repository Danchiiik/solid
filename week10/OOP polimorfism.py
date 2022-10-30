#! Полиморфизм - возмодность импользовать один и тот же метод для обьектов от разных классов, при этом результат может меняться в зависимости к какому классу принадлежит обьект.
# Полиморфизм - множество форм

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         print('Meeeeow')
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def make_sound(self):
#         print('Gav')
#
#
# cat1 = Cat('Barsik')
# dog1 = Dog('Rex', 20)
#
# # cat1.make_sound()
#
#
# list_obj = [cat1, dog1]
# for i in list_obj:
#     i.make_sound()


# class ShapeMixin:
#     def __init__(self, name):
#         self.name = name

#     def area(self):
#         pass

#     def __str__(self) -> str:
#         return self.name

# class Square(ShapeMixin):
#     def __init__(self, name, h):
#         super().__init__(name)
#         self.h = h

#     def area(self):
#         return self.h **2


# class Circle(ShapeMixin):
#     def __init__(self, name, radius):
#         self.name = name
#         self.radius = radius

#     def area(self
#         return 3.14*self.radius **2

# s1 = Square('square', 10)
# s2 = Square('square2', 2)
# c1 = Circle('circle', 2)
# c2 = Circle('circle', 3)
# print(s1)
# print(s2)


# class A:

#     def __init__(self, n, a) -> None:
#         self.name = n
#         self.age = a
        
#     def __str__(self) -> str:
#         return self.name

# a1 = A('Sam', 12)
# print(a1)
class MyStr(str):
    def upper(self):
        return 'John'

    def __str__(self) -> str:
        return super().__str__() + ' John'


str1 = MyStr('hello')
print(str1)
