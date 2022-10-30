
#! Основные принципы ООП: Наследование

# class A:
#     a = 2

# class B(A):
#     pass

# obj_a = A()
# print(obj_a.a)
# obj_b =B()
# print(obj_b.a)


# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def get_info(self):
#         return f'Hello, my name is {self.name}, i am {self.age}'

# class Student(Person):
#     def __init__(self, name, age, kurs) -> None:
#         # Person.__init__(self, name, age)
#         super().__init__(name, age)
#         self.kurs = kurs

#     def get_info(self):
#         return super().get_info() + f' and {self.kurs}'



#     def study(self):
#         return 'I am studying'

# Nurik = Student('Nurik', 16, 2)
# print(Nurik.get_info())
# print(Nurik.study())
# # sam = Person('John', 22)
# # print(sam.get_info())


# class A:
#     def __init__(self, name) -> None:
#         self.name = f'Name: {name}'

# class B(A):
#     def __init__(self, name, age) -> None:
#         super().__init__(name)
#         self.age = age


# obj = B('John', 22)
# print(obj.name, obj.age)


# print(isinstance(1, int)) #? Проверяет является ли обьект, экземпляром данного класса
# print(issubclass(int, str)) #? Функция проверяет является ли класс подклассом второго аргумента 
# print(issubclass(int, object))

# class A:
#     pass

# class F(A):
#     pass

# print(issubclass(A, object))
# print(issubclass(F, object))


# class MyStr(str):
#     def __str__(self) -> str:
#         return super().__str__() + ' John'

#     def upper(self):
#         return 'Bye'

# s = MyStr('hello')
# print(s)
# print(s.upper())






