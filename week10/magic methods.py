
#!Магические методы (Дандер методы, супер методы, служебные методы).

#?Магисеские методы - это в первую очередь те методы у которых два нижних подчеркивания в начале и в конце, срабатывают эти методы автоматически при выполнении какой-то операции (+,-,<>, / и т.д.), мы можем добавлять какой-то функционал - свою логику

#?Магические методы необходимы для того, чтобы определяемые объект могли работать с некоторыми операторами или же встроенными функциямии


# class User: 
#     def __new__(cls, *args, **kwargs): 
#         print('new worked')
#         return super().__new__(cls)

#     def __init__(self,email) -> None:
#         print("Init worked")
#         self.email = email

#     def __str__(self) -> str:
#         return self.email

#     def __del__(self):
#         print('deleted')



# user1 = User("admin@admin.com")
# print(user1)
# del user1
# print('fff')


# class Word(str):
#     def __new__(cls, *args, **kwargs):
#         s = args[0]
#         s = s.replace(' ', '')
#         return super().__new__(cls, s, )

# word1 = Word('a b c')
# print(word1)


# class User:
#     def __init__(self, email) -> None:
#         self.email = email

#     def __str__(self) -> str:
#         return self.email

#     def __repr__(self) -> str:
#         return self.email

# user1 = User('Dan')
# print(user1)

# a = 'sad'

# a = 'input()'
# print(a)
# eval(a)


# import datetime
# print(repr(datetime.date.today()))


# class MyNumber(int):
#     def __init__(self, value) -> None:
#         self.value = value

#     def __add__(self, other: int) -> int:
#         return f'Это + и результат равен: {self.value + other}'

#     def __sub__(self, other: int) -> int:
#         return f'Это - и результат равен: {self.value - other}'

#     def __mul__(self, other: int) -> int:
#         return f'Это - и результат равен: {self.value * other}'

#     def __truediv__(self, other: int) -> int:
#         return f'Это / и результат равен: {self.value / other}'

#     def __floordiv__(self, other: int) -> int:
#         return f'Это // и результат равен: {self.value // other}'

#     def __mod__(self, other: int) -> int:
#         return f'Это % и результат равен: {self.value % other}'

#     def __pow__(self, other: int) -> int:
#         return f'Это ** и результат равен: {self.value ** other}'

#     def __radd__(self, other: int) -> int:
#         return f'Это + и результат равен: {self.value + other}'

# num = MyNumber(5)
# print(num + 1)
# print(num - 1)
# print(num * 2)
# print(num / 2)
# print(num // 2)
# print(num % 2)
# print(num **2)
# print(2 + num) #! 'r'
# #* radd, dsub ....

# num += 1 #! 'i'
# #* iadd, isub


# class Employee:
#     def __init__(self, name, salary, rating) -> None:
#         self.name = name
#         self.salary = salary
#         self.rating = rating

#     def __gt__(self, other): #*greater than
#         return self.rating > other.rating

#     def __lt__(self, other): #* less than
#         return self.rating < other.rating

#     def __eq__(self, other) -> bool:
#         return self.rating == other.rating

#     def __ge__(self, other):
#         return self.rating >= other.rating

#     def __le__(self, other):
#         return self.rating <= other.rating

#     def __ne__(self, other) -> bool:
#         return self.rating != other.rating

# john = Employee('John', 35, 9)
# sam = Employee('Sam', 40, 10)
# print(john > sam)

# class NewClass:
#     def __init__(self, name) -> None:
#         self.name = name

#     def __int__(self):
#         print('hello')
#         return 100

#     def __bool__(self):
#         print('Hello')
#         return True

# a = NewClass('5')
# print(int(a))
# print(bool(a))



# class A:
#     def __setattr__(self, name, value) -> None:
#         value = value.upper()
#         return super().__setattr__(name, value)

#     def __delattr__(self, name: str) -> None:
#         print('deleted')
#         return super().__delattr__(name)

# obj1  = A()
# obj1.f = 'John'
# del obj1.f
# print(obj1.f)


# class A:
#     def __init__(self) -> None:
#         self.l = [1, 2, 3]

#     def __getitem__(self, index):
#         return self.l[index]

#     def __setitem__(self, index, value):
#         self.l[index] = value

#     def __delitem__(self, index):
#         return 'i deleted'

# a = A()
# # print(a[0])
# a[0] = 'Hello'



# class A:
#     def __init__(self, age, name) -> None:
#         self.age = age
#         self.name = name
#         self.__l = []

# obj1 = A(name = 'john', age = 22)
# print(obj1.__dict__)


#* __getattr__ 
#* __getattribute__

# nums = [8, 1, 2, 2, 3]
# a = []
# b = 0
# for i in nums:
#     for j in nums:
#         if i > j:
#             b += 1
#     a.append(b)
#     b = 0
# print(a)


class MyString(str):
    def __init__(self, str_):
        self.str_ = str_

    def append(self, str_append):
        self.str_ += str_append

    def pop(self):
        res = self.str_[-1]
        self.str_ = self.str_[:-1]
        return self.str_[-1]
    
    def __str__(self) -> str:
        return self.str_

example = MyString('String') 
example.append('hello') 
print(example) 
print(example.pop())


        