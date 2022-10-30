
#! Множественное наследование и миксины

# class A:
#     name = 'John'

#     def __init__(self, age):
#         self.age = age 
#         self.is_alive = True

#     def move(self):
#         return 'Go go go'

# class B(A):
#     name = "Sam"

#     def move(self):
#         return super().move() + 'Hello'

# b = B(30)


# class Call:
#     def call(self):
#         return ('Call...')

# class Mail:
#     def send_mail(self):
#         return 'Message is sending'

# class Smartphone(Call, Mail):
#     ...

# p1 = Smartphone()
# print(p1.call())
# print(p1.send_mail())
# print(isinstance(p1, Smartphone))
# print(isinstance(p1, Call))
# print(issubclass(Smartphone, Mail))


# class Parent1:
#     a = 10
    

# class Parent2:
#     a = 15
    

# class Child(Parent1, Parent2):
#     a = 20

# obj = Child()
# print(obj.a)
# print(Child.mro())

#? MRO - это method resolution order (порядок разрешения методов)


# class A:
#     a = 1

# class B(A):
#     a = 2

# class C(A):
#     a = 3

# class D(C, B):
#     a = 4

# d = D()
# # print(d.a)

# print(D.mro())


# class Grandpa:
#     a = 1

# class Grandma:
#     a = 2

# class Dad(Grandpa, Grandma):
#     a = 3

# class Mom:
#     a = 4

# class Me(Dad, Mom):
#     a = 5




#! Mixin

# Миксины это особый вид множественного наследования. Задачей миксинов является расширение функциоанала других классов (расширение классов)
# Работа с Mixin
#1. принято давать имена заканчивающиеся на Mixin: SendMailMixin
#2. От Mixin классов нельзя создавать обьекты
#3. Нужны чтобы расширить функционал другого класса (добавляя новую логику)


# class MoveMixin:
#     def move(self):
#         print('move mf')

# class StopMixin:
#     def stop(self):
#         print('stop mf')



# class Car(MoveMixin, StopMixin):
#     pass

# class Person(MoveMixin, StopMixin):
#     pass


# class PersonInitMixin:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

# class GetInfoMixin:
#     def info(self):
#         print(self.name, self.age)

# class GetYearMixin:
#     def get_year(self):
#         print(2022 - self.age)
        

# class Person(PersonInitMixin, GetInfoMixin, GetYearMixin):
#     ...

# sam = Person('john', 12)
# sam.get_year()


n = 19
# a = []
# for i in str(n):
#     a.append(int(i))
        
# b = 0
# while sum(b) != 1:
#     a = [i**2 for i in a]
#     b = sum(a)
            
# print(True)

