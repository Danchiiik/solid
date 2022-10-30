
#! Оператор Try - Except  обработка исключений


#? Ошибки - проблема в синтаксисе

#* SyntaxError - ошибки в синтаксисе кода
# 2f = 45

#* IndentationError - неправильный отступ
# name = 'John'
    # name

#* TabError - смешивание пробелов и табов
#----
#____ 




#? Исключения - проблема в синтаксисе которую можно решить

#* ZeroDivisionError
# 2/0

#* NameError (name isnt defined)
# name

#* TypeError (type if object doesnt match to operation)
# '2' + 2

#* ValueError (value of object doesnt match to operation)
# s = 'H'
# int(s)

#* IndexError (appeal to unexisted object)
# l = [1]
# l[100]

#* KeyError (appeal to unexisted key)
# d = {1:1}
# d['John']

#* ImportError (wrong import)
# from math impot pi2

#* ModuleNotFoundError 
# from math2 import pi

#* AttributeError (try to call unexisted method or attrubute of object )
# x = 2
# x.isdigit()

#* KeyboardInterrupt (when user press certain keys of keyboard)
# while True:
#    print('John')





# print('Hello world')
# x = int(input("enter the 1-number: "))
# y = int(input('enter the 2-number: '))
# print(x / y)


# print('Hello')
# a = 5
# b = 'AAAA'
# try:
#     name
#     print(a/b)
# except (ZeroDivisionError, NameError):
#     print('dont divide by 0')
#     print('fuck off man')
# except:
#     print('any error except Zero, Name errors')
# # except NameError:
#     # print('Fuck off man')
# print('******************')



# n = int(input("1: ") )
# n2 = int(input('2: '))

# try:
#     n = int(input("1: ") )
#     n2 = int(input('2: '))

#     print(n/n2)
# except ZeroDivisionError:
#     print('aa')
# except TypeError:
#     print('aa')
# except NameError:
#     print('aa')
# except ValueError:
#     print('aa')

# try:
#     while True:
#         print('12345')
# except KeyboardInterrupt:
#     pass
# print('hello')

# try:
#     4/0
# except Exception as e:
#     print(e)


# try: # try to do something
#     pass
# except NameError: # work when in 'try' happened error
#     pass
# else: # if errors doesnt happened 
#     pass
# finally: # work in any case at the end 
#     pass

# try:
#     print(5/8)
    
# except ZeroDivisionError:
#     print('dont do it man')
# else:
#     print('Well done')
# finally:
#     print('Bye')

# name = 'John'
# if name == "John":
#     raise Exception ('You are John')

# age = 10
# try:

#     if age<18:
#         raise ValueError('you are shigol')
# except ValueError as e:
#     print(e)


# a = {'a':1, 'b':5, 'c': 4, 'd': 3}
# dict_ = {i:[range(1, len(i)+1)] for i in a}
# print(dict_)


# a = {'history': 90, 'math': 95, 'literature': 91}
# print(a.items())
# s = {i for i in list(a.keys()) if i['math']}
# print(s)

# set1 = {i for i in range(10)}
# set2 = {i for i in range(8, 15)}
# full_set = set1.union(set2)
# col = len(set1.intersection(set2))
# coll = len(full_set)
# print(f"В этом сете было {col} повторения, его длинна составляет {coll}" if coll<20 else "Ваш обьединенный сет полностью уникальный!" )


inp1 = input()
inp2 = input()
if type(inp1) !=int and type(inp2) !=  int:
    print(str(inp1) + str(inp2))
else:
    print(inp1+inp2)