
#!  Основные принципы ООП: Инкапсуляция

# 1) Обьединение всех свойств и методов в одну капсулу или же класс
# 2) Ограничение доступа к переменным или методам для сокрытия данных от внешнего воздействия

# 3 модификатора доступа: 
#? public - публичный (данные доступны всем)
#? _protected - защищенный (данные доступны только внутри этого класса или же у дочерних)
#? __private - самый защищенный (доступно только внутри класса)

# class A:
#     name = 'John' # pubic
#     _age = 20 # _protected
#     __surname = 'Snow' #__private

# obj = A()


# class A:
#     def name(self):
#         return 'Dan'

#     def _age(self):
#         return 20

#     def __surname(self):
#         return 'asdfgh'

# ibj = A()
# print(ibj.name())
# print(ibj._age())
# print(ibj._A__surname())


# class Person:
#     name = 'John'
#     _age = 20
#     __last_name = 'Snow'

# class Student(Person):
#     def get_info(self):
#         print(self.name)
#         print(self._age)

# o = Student()
# print(o.get_info())



# class Game:
#     __level = 0

#     def get_level(self):
#         return self.__level

#     def set_level(self, new_level):
#         self.__level = new_level

# obj = Game()
# # print(obj.get_level())
# print(obj.set_level(10))
# print(obj.get_level())


# #? priority and setter

# class ReadFile:
#     def read_file(self, file_name):
#         with open(file_name, 'r')as file:
#             return file.read()

# class WriteFile:
#     def write_file(self, file_name, straa):
#         with open(file_name, 'w')as file:
#             file.write(straa)
#             file.write('\n')

# class WriteAppendFile:
#     def write_append_file(self, file_name, straa):
#          with open(file_name, 'a')as file:
#             file.write(straa)
#             file.write('\n')

# class John(ReadFile, WriteFile, WriteAppendFile):
#     name = 'John'
#     def __init__(self, file_name):
#         self.file_name = file_name


# john  = John('info.txt')
# print(john.read_file(john.file_name))
# print(john.write_append_file(john.file_name, 'Pochka Nurika'))


#?###################3


# class Game:
#     _level = 0

#     @property
#     def level(self):
#         return self._level

#     @level.setter
#     def level(self, new_level):
#         self._level = new_level

#     # def get_level(self):
#     #     return self._level

#     # def set_level(self, new_level):
#     #     self._level = new_level
#     #     return new_level

# obj = Game()
# print(obj.level)
# obj.level = 2
# print(obj.level)
# print(obj.set_level(2))
# print(obj._level)


# class Person:
#     name = 'Dan'
#     _phone_number = '+996 701 75 07 07'
#     __card_number = '9999 9999 9999 9999'


# john = Person()

# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)


# class Person:

#     def __init__(self, name, _phone_number, __card_number):
#         self.name = name
#         self._phone_number = _phone_number
#         self.__card_number = __card_number

# john = Person('John', '+996 701 75 07 07', '9999 9999 9999 9999')
# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)


# class Person:
#     name = 'Dan'
#     _phone_number = '456788765'
#     __card_number = '345678654'

# john = Person()
# john.name = None
# john._phone_number = None
# john._Person__card_number = None

# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)

# class Person:

#     def __init__(self, name, _phone_number, __card_number):
#         self.name = self.__validate_name(name)
#         self._phone_number = _phone_number
#         self.__card_number = __card_number

#     def __validate_name(self, name):
#         return 'John' if len(name) <2 else name.title()


# sam = Person('sam', '345677654', '34567654')
# print(sam.name)
# print(sam._Person__validate_name())



# 5) На этот раз заказчик передумал и попросил вас переписать предыдущий класс, теперь его интересует только валидация номера телефона и номера карты. Создайте класс Person у которого будут следующие атрибуты экземпляра класса: name (public), phone_number(protected) и сard_number(private). При инициализации обьекта проверяйте введенный номер телефона и номер карты. Для этого напишите приватный метод validate_phone_number и защищенный метод validate_cart_number.
# Метод validate_phone_number сначала проверяет на то чтобы номер телефона являлся типом int иначе возвращаем None далее нужно также проверять, чтобы номер начинался на 999 иначе возвращается None
# Метод validate_cart_number в первую очередь также проверяет то что бы номер карты являлся типом int иначе возвращаем None далее нужно также проверять что чтобы количество цифр в номере карт была ровно 16 иначе также возвращаем None. Создайте экземпляр 'tolik' класса Person c правильными данными и выведите на экран все его атрибуты

# class Person:

#     def __init__(self, name, phone_number, card_number):
#         self.name = name
#         self._phone_number = self.__validate_phone_number(phone_number)
#         self.__card_number = self._validate_card_number(card_number)

#     def __validate_phone_number(self, number):
#         if type(number) != int or str(number).startswith('996'):
#             return None
#         return number

#     def _validate_card_number(self, card_number):
#         if type(card_number) != int or len(str(card_number)) != 16:
#             return None
#         return card_number


# tolik = Person('sam', 996995750707, '9999999999999999')
# print(tolik.name)
# print(tolik._phone_number)
# print(tolik._Person__card_number)


# class Person:
#     __name = 'John'

#     @property
#     def name(self):
#         return self.__name


#     # def get_name(self):
#     #     return self.__name

#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
    
#     # def set_name(self, new_name):
#     #     self.__name = new_name

# j = Person()
# print(j.name)
# j.name = 'Dan'
# print(j.name)


# class MyDict(dict):
    
#     def get(self, key):
#         return self.keys()
#         # if key in self:
#         #     return self[key]
#         # # return 'NO'
#         # if key != self[]
#         #     return 'No'
#         # return self[key]

# d = MyDict({'a': 2})
# print(d.get('a'))

nums = [1, 2 , 6, 7, 8, 9, ]
a = len(nums)
b = []
for i in range(1, a+1):
    if i in nums:
        continue
    else:
        b.append(i)
print(b)        