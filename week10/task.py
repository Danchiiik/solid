
# class Cat:
#     is_alive = True
#     a = 1
#     _b = 2
#     __c = 3

#     @property
#     def c(self):
#         return self.__c


#     @c.setter
#     def c(self, new):
#         self.__c = new

#     def __new__(cls, *args, **kwargs):
#         print('я сработал')
#         return super().__new__(cls)

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self) -> str:
#         return self.name
    
#     def go(self):
#         return 'Иду'

#     def info(self, last_name):
#         return f'I am {last_name} {self.name}, i am {self.age}'

#     def make_sound(self):
#         return 'meoww'

# obj = Cat('Dan', 12)
# print(obj.name)

# print(obj.go())
# print(obj.info('Sab'))
# print(obj.make_sound())

# print(obj.a)
# print(obj._b)
# print(obj._Cat__c)

# obj._Cat__c = 5
# print(obj.c)


# class Dog:

#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         return 'gav'

# obj2 = Dog('Nurik')


# for i in [obj, obj2]:
#     print(i.make_sound())


# class Barsik(Cat):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
        

# aa = Barsik('aa', 34, 'black')
# print(aa.color)


# class ToDo:
#     inctances = {}

#     def __init__(self, tasks) -> None:
#         self.tasks = tasks

#     def give_priority(self, priority):
#         self.inctances[priority] = self.tasks

#     def list_of_task(self):
#         return sorted(self.inctances.items())



# obj1 = ToDo('сходить в кино')
# obj2 = ToDo('сделать домашку')
# obj3 = ToDo('поиграть')
# obj1.give_priority(3)
# obj2.give_priority(2)
# obj3.give_priority(1)

# print(obj1.list_of_task())

# l = [{'id':1}, {'id':2}, {'id':3}, {'id':4}, {'id':5}]

# def get_product(list_, page=1):
#     page -=1
#     res = [[]]

#     page_index = 0
#     count_ = 0

#     for i in list_:
#         if count_ == 2:
#             res.append([])
#             page_index +=1
#             count_ = 0

#         count_ += 1
#         res[page_index].append(i)
#     return res[page]

# print(get_product(l, 3))

# class MyString(str):

#     def __init__(self, str_) -> None:
#         self.str_ = str_

#     def append(self, new_str):
#         self.str_ += new_str

#     def pop(self):
#         last_s = self.str_[-1]
#         self.str_ = self.str_[:-1]
#         return last_s


#     def __str__(self) -> str:
#         return self.str_


# obj = MyString('String')
# obj.append('hello')
# # print(obj)
# #
# print(obj.pop())
# print(obj)
