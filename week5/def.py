
#! Введение в функции. Позиционные и именованные, args? kwargs  параметры по default 


# def hello(x, y):
    
#     return x + y

# print(hello(2, 4))

#* Встроенные функции() - sum, len, print, max, dir, int


# def get_mult(x, y, z): # Параметры
#     s = x*y*z

#     print(s)


# get_mult(3, 4, 5) # Аргументы


#* Аннотации функций
# def func(x: int, y: str) -> int:
#     return x + y

# print(func( 2, 4 ))


#* параметры по default
# def func2(x = 'Tolik'):
#     return x + ' Hello'
# print(func2('John'))
# print(func2())

# def func3(x:int, y:int, z:int = 2):
#     return x+y+z
# print(func3(2, 4))



# list_ = [1, 2, 3, 4]

# def sm(l):
#     s = 0
#     for i in l:
#         s += i
#     return s
# print(sm(list_))


#*  Позиционные и именованные аргументы

# def func(x, y, z):
#     print(x, y, z)
#     pass
# func(2, 3, 5) # позиционные аргумкенты
# func(y = 5, z = 2, x = 3) # именованные аргументы
# #func(y = 4, 4, 5) #! Error ( после им. нельзя ввести поз. аргументы)
# func(5, z = 2, y = 4) #? Succeed


# *args  and **kwargs - позиционные и именованные аргументы


# def func5(x, y, *args, **kwargs) :
#     print(args) # tuple
#     print(kwargs) # dict
#     return x + y + sum(args) + sum(kwargs.values())

# print(func5(5, 4, 5, 6, 7, 7, c=6))



# def op(x, y):
#     a  = list(range(x, y+1))
#     return a
# print(op(3, 7))

# def f():
#     if False:
#         return 'f'
#     else:
#         return 't'
# print(f())

# a = [3, 4, 6, 7]

# def fun(z, *a, **aa):
#     print((z, a))

# fun(a, 1, 2, 4, 6)

# for i in range(1, 100, 2):
#     if i == 5:
#         continue
#     elif i == 9:
#         break
#     print(i)

# list_ = range(1, 100, 2)
# i = 0
# while i<100:
#     print(list_[i])
#     i += 1

# def pl(x, y):
#     return x+y
# print(pl(3, 6))


# def plus(x:int, y:int = 5, *args, **kwargs):
#     return x + y + sum(args) + sum(kwargs.values())
# print(plus(1,  c = 1))


# try:
#     a = int(input())
#     def is_even(x):
#         if x%2 == 0:
#             return True
#         else:
#             return False
#     print(is_even(a))
# except:
#     print('looooooox')


# def validate_email(email):
#     if not '@' in email:
#         raise Exception('where is @ ?')

#     elif not email.endswith('.com'):
#         raise Exception("where is .com ?")

#     elif not len(email)>= 10:
#         raise Exception('so short email')
#     else:
#         return "correct"
# print(validate_email('d@gil.com'))

def foo():
    var = 'переменная foo'
    print(var)
  
    def bar():
        global var
        var = 'переменная foo'
        print(var)
    bar()

    
print('переменная в foo:',  foo())
# print('переменная в foo:',  bar())






#list_ = ['admin@admin.com', '1@1.com', '23@gmail.com'] 

balance = 0
def get_salary(a):
    global balance
    balance += a

def pay_bills(a, l):
    global balance
    balance -= a
