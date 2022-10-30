
#! ООП - обьектно ориентированное программирование, парадигма программирования в котором все основывается на двух ключевых понятиях - класс и обьект

# класс - дает нам общюю харак. которую будут использовать его обьекты

# обьект - экземпляр класса


# class MyFirstClass:
#     string = 'hello' # атрибут класса
    
#     def first_method(self):
#         return 'I am method'

# obj1 = MyFirstClass()
# obj2 = MyFirstClass()
# print(obj1.string)
# print(obj1.first_method())
# print(dir(obj1))


# class Animal:
#     is_alive = True
#     def __init__(self, name, age): #self - ссылка на обьект
#         self.name = name # атрибут обьекта
#         self.age = age

#     def move(self, info):
#         return f'Hello, I\'m {self.name} {info}'


# cat = Animal('max', 13)
# dog = Animal('bobik', 10)
# print(cat.name) #max
# print(dog.name) #bobik
# print(cat.move('meoow'))

# class A:
#     x = 5

#     def __init__(self, name):
#         self.name = name

# obj1 = A('Pochka Nurika')
# obj2 = A('Ruka Ulika')
# obj3 = A('Ochki Dani ')
# obj1.x = 12345 
# obj1.name = 'Sam Nurik'
# print(obj1.x)
# print(obj2.x)
# print(obj3.x)
# print(obj1.name)

# obj1.y = 10
# print(obj1.y) 

# class Human:
#     is_alive = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def br(self):
#         self.age += 1
#         print(f'Happy Birthday {self.name}, now you are {self.age}')
    
# john = Human('John', 22)
# print(john.name)
# john.br()
# john.br()


# class Student:
#     cash = 100

#     def __init__(self, name, course):
#         self.name = name
#         self.course = course

#     def spend_money(self, sum):
#         sum = int(input('aaa: '))
#         self.res = self.cash - sum
#         if self.res < 0:
#             raise Exception(f'{self.name} dont do it')
#         self.cash -= sum
#         return self.cash

# john = Student('John', '1')
# print(john.spend_money(sum))
# print(john.spend_money(sum))
# print(john.spend_money(sum))
# print(john.spend_money(sum))



# class Car:
    
#     def __init__(self, name, color, year) -> None:
#         self.name = name
#         self.color = color
#         self.year = year        

#     def info(self):
#         return 'I am car'

#     def go(self, speed):
#         return f'I am {self.name}, {self.year} year and go {speed} km/h'

# car1 = Car('BMW', 'green', 2000) 
# print(car1.name)
# print(car1.go(40))
# # print(car1.info())

# class Student:
#     def __init__(self, name, surname) -> None:

#         self.name = name
#         self.surname = surname
#         self.knowledge = 0
        

#     def read_book(self, hours):
#         if hours >= 10:
#             self.knowledge -= 10
#             return('ai ai ai, don\'t lie')
        
#         self.knowledge += 5 * hours
#         return f'Well done, you have read {hours} hours, and now your knowledge is {self.knowledge}' 


# John = Student('John', 'Snow')
# print(John.knowledge)
# print(John.read_book(30))
# print(John.read_book(5))
# print(John.knowledge)







# class Instagram:
#     def __init__(self, username, password) -> None:
#         self.name = username
#         self.password = password
#         self.posts = []
#         self.id = 0

#     def get_posts(self):
#         return self.posts

#     def create_post(self, title, desc):
#         post = dict(id = self.id, title = title, desc = desc)
#         self.posts.append(post)
#         self.id += 1
#         return 'well done'

#     def delete_post(self, id):
#         for post in self.posts:
#             if post.get('id') == id:
#                 index_ = self.posts.index(post)
#                 self.posts.pop(index_)
#                 return 'deleted'
#             return 'not found'

#     def update_post(self, id, **kwargs):
#         for post in self.posts:
#             if post.get('id') == id:
#                 index_ = self.posts.index(post)
#                 self.posts[index_].update(**kwargs)
#                 return 'updated'     

    

# john = Instagram('John2022', '123')
# print(john.create_post('aaaaa', 'ghj'))
# print(john.create_post('ass', 'g'))
# print(john.create_post('ahhhaa', 'dfg'))
# print(john.delete_post(2))
# print(john.update_post(0, title ='Dancho' ,desc='danchiik'))
# print(john.get_posts())




class MyString(str):

    def __init__(self, name):
        self.name = name


    def append(self, str_):
        return self.name + str_

    def pop(self):
        return self[0:-2]

    def __str__(self) -> str:
        return self.name + str_


example = MyString('String')
print(example.append('hello'))
print(example)