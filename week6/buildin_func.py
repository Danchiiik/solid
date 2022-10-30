
#! Встроенные функции map, filter, reduce, zip, enumerate, all, any

# print(all([True, False]))
# print(all([True, True]))


# print(any([1, 0]))
# print(any([True, False]))


# a = lambda x: str(x)
# print(a(5))


#!map - функция нужна для того чтобы применить какую либо функцию к другим значениям.
#Синтаксис map(func, iter_type)

# list_ = [1, 2, 3, 4, 5]
# # res = map(lambda x: str(x), list_)
# # print(list(res))

# res = list(map(str, list_))
# print(res)


# def func(x):
#     return str(x)

# res = list(map(func, list_))
# print(res)


# l = [1, 2, 3, 4]
# s = list(map(lambda x: x+3, l))
# print(s)

# a = lambda x: x+5 if x%2 == 0 else x+2
# print(a(2))

# l = [1, 2, 3, 4, 5]
# res = list(map(lambda x: 'even' if x%2 ==0 else 'odd', l))
# print(res)

#! filter
# l = [1, 2, 3, 4, 5, 6]
# # r = list(filter(lambda x: x%2 == 0 , l))
# # print(r)

# # def func(x):
# #     return x%2 == 0

# # r = list(filter(func, l))
# # print(r)


# l = range(100)
# a = list(filter(lambda x: x%3 == 0, l))
# print(a) 


#! reduce

# l = [1, 2, 3, 4, 5, ]

# from functools import reduce
# # res = reduce(lambda x, y: x+y , l)
# # print(res)


# # def func(x, y):
# #     return x+y

# # res = reduce(func, l)
# # print(res)

# res = reduce(min, l)
# print(res)


#! zip 
# l = {1, 2, 3, 4}
# l2 = {'a', 'b', 'c'}
# l3 = {'john', 'snow'}
# res = list(zip(l, l2, l3))
# print(res)


#! enumerate

# l = ['john', 'Tolik', 'Sam', 'Rachel']
# r = list(enumerate(l, 10))
# r = list(enumerate(l))
# print(r)

# list_ = [1, 5, -9, 6, -4]
# result = not any(list_)
# print(result)

# from functools import reduce 
# list_ = ['qqw', 'ertygf', 'dhytresfg']
# result = reduce(lambda x, y: x if x>y else y, list_)
# print(result)

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = list(map(lambda x: [x], l))
# print(res)


#! функция высшего порядка - это функция  которая может принимать в качестве аргумента другую функцию и возвращать другую функцию как рез. работы

# l = [(1, 2, 3), ('hello', 'john', 'snow')]
# for i, i2, i3 in l:
#     print(i, i2, i3)

# l = ['a', 'b', 'c', 'd', 'f']
# # for i in l:
# #     print(f'{i} - {l.index(i)}')

# for i, j in enumerate(l):
#     print(i, j)

# def map_(func, it_ob):
#     new_list = []
#     for i in it_ob:
#         new_list.append(func(i))
#     return(new_list)


# l = [1, 2, 3]
# print(map_(lambda x: str(x), l))


# def filter_(func, it_ob):
#     new_list = []
#     for i in it_ob:
#         if func(i):
#             new_list.append(i)
#     return new_list

# l = [1, 2, 3, 4]
# print(filter_(lambda x:x%2 == 0  , l))

# nums = [1, 2, 3]

# nums += nums
# print(nums)
# operations = ['--x']
# count = 0
# for i in operations:
#     if i == '--x' or i == 'x--':
#         count -= 1
#     elif i == '++x' or  i =='x++':
#         count += 1
# return

from functools import reduce
# l = [1, 2, 3, 4, 5]
# res = list(map(lambda x: x<5, l))
# res2 = list(filter(lambda x: x<5, l ))
# print(res)
# print(res2)

# l = [1, 2, 3, 4]
# res = reduce(lambda x, y: x*y, l)
# print(res)

# l = 'John'
# r = [i*3 for i in l]
# print(r)

# import random

# r = [random.randint(-10, 10) for i in range(10) ]
# l = [abs(i) for i in r ]

# print(r , l)

# l = ['abs!$@', '12343424$$$$$', '*&*' ]
# symbols = '!@#$%^&*()-_=+[]{}\|/?'
# def clear_(str_):
#     new_l = ''
#     for i in str_:
#         if i in symbols:
#             continue
#         else:
#             new_l += i
#     return new_l


# r = list(map(clear_, l))
# print(r)

# vowels = 'aeiou'
# s = 'Hello world! How are you today!'

# def count_(s):
#     new_l = {}
#     for i in s:
#         if i in vowels:
#             new_l[i] = s.count(s[i]) 
#     return new_l
# print(count_(s))


# boss = 100

# def boss2():
#     global boss
#     boss2 = 70
#     size2 = boss + boss2
    

#     def boss3():
#         nonlocal size2
#         boss3 = 50
#         size3 = size2 + boss3
#         print(size3)
    
#     boss3()
# boss2()

l = []

def add():
    s = input('')
    l.append(s)
    


def remove():
    i = int(input('index: '))
    s = input('')
    a  = l.insert(i, s,)
    l.pop(a)
    

add()
remove()
add()
add()
remove()
add()
remove()
add()
add()
remove()
print(l)
