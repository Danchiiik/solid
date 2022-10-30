
#! Декораторы в Python 

# Декоратор - это функция которая в свою очередь принимает другую функцию. Декоратор позволяет обернуть другую функцию для расширения ее без изменения ее кода.



# def decorator_func(func):
#     def wrapper(some_data):
#         return f'вы передали: {func(some_data)}'
#     return wrapper

# @decorator_func
# def get_name(name):
#     return name

# def get_last_name(last_name):
#     return last_name

# def get_age(age):
#     return age

# print(get_name('asddgfds542646'))

# def func_dec(f):
#     def wrapper():
#         print('I am code which will run before func1')
#         f()
#         print('I am code which will run after func1')
#     return wrapper

# @func_dec
# def func1():
#     print('I am function func1')


# func1()

# def decorator(f):
#     def wrapper(*a, **k):
#         print('Hello')
#         f(*a, **k)
#         print('bye')
#     return wrapper

# @decorator
# def fun_without_params():
#     print('Func without params')

# @decorator
# def fun_with_params(name, last_name):
#     print('func with params')
#     print(name, last_name)

# fun_without_params()
# fun_with_params('john', 'snow')


# def div_dec(f):
#     def wrapper(*args, **kwargs):
#         print(f.__name__)
#         return f'<div> {f(*args)} </div>'
#     return wrapper

# @div_dec
# def get_info(name, lastname):
#     res = 2+2
#     return f'{name} {lastname}{res}'

# print(get_info('John', 'Snow'))


# def dec_aa(f):
#     def wrapper(s):
#         print(f'Result is {f(s)}, and {f(s)} is {"even" if f(s)%2==0 else "odd"} number')
#     return wrapper



# @dec_aa
# def get_sum(list_):
#     res = 0
#     for i in list_:
#         res += i
#     return(res)

# get_sum([1, 3, 3])



# def decorator_func(func):
#     print('hello John')
#     return func

# @decorator_func
# def func():
#     return 'Hey'

# # res = decorator_func(func)
# # print(res)
# print(func())

# def to_upper_dec(fun):
#     def wrapper():

#         #res = fun()
#         return 'fff'
#     return wrapper

# @to_upper_dec
# def get_name():
#     return 'John'

# @to_upper_dec
# def get_last_name():
#     return 'Snow'

# print(get_name())












