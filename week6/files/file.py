
#! Файлы. Модули. Import(from). Работа с файлами (чтение и запись)

#! Модуль - это файл .py который содержит некоторые функции и переменные. При необходимости они могут быть импортированы.

# (math, this, random, time)

#! Пакет - состоит из модулей, испю для того чтобы упаковать файлы для удобства хранения и управление. Первым файлом в пакете является __init__.py


#! Библиотека - это просто набор модулей, пакетов, функций.

# import math
# print (math.pi)

# pi = 'dsafsf'
# from math import pi as pi2
# print(pi2)
# print(pi2)

#from math import * # импортировать все



# from helper import age, get_name
# # print(age)
# print(get_name('joni'))



#! При помощи Python можно работать с файлами (создавать, добавлять, считывать, изменить)

#! open() - встроенная функция позваляющая открыть какой то файл

#! read()
# file = open('test.txt', 'r')
# print(file.tell()) # говорит где находится курсор
# print(file.read()) # читать содержимое
# print(file.tell())
# print('**')
# file.seek(9)
# print()
# print(file.read())
# file.close()


# f = open('test.txt')
# # data = f.read(6)

# # print(data)
# # print(f.read())
# # print()
# # print(f.readline()) # читает одну строку
# # print(f.readlines()) # возвращает список со всеми элементами

# for i in f:
#     print(i)

# f.close()


#! write()
# 'w' - открывает запись, содержимое файла удаляется, если файла не сущ. то создается новый.


# file = open('test2.txt', 'w')
# # file.write('pochka Nurika tut')
# # file.write(str(18)) # ожидает строку
# file.writelines(['a\n', '\ts']) #ожидает коллекцию
# file.close()

# # try:
# #     f = open('test.txt')
# # finally:
# #     f.close()

# with open('test.txt') as file: 
#     print(file.read())
# print(file.read())

#! append() 
# 'a' - добавь что то 
# with open('test3.txt', 'a') as file:
#     file.write('hello')


# with open('test.txt', 'r') as file:
#     print(file.read())

#     with open('test.txt', 'a') as file2:
#         file2.write('\nsnow')

# with open('task3.txt', 'r+') as file:
#     l = [int(i) for i in file.readlines() if  i != '\n' ]
#     ma = max(l)
#     mi = min(l)
    
# fil = open('task6.txt', 'w+')
# fil.write(f'{mi}-{ma}')
# fil.seek(0)
# print(fil.read())
# fil.close()
# 


# with open('task3.txt', 'r+') as file:
#     res = file.readlines()
#     res = [int(i.replace('\n', '')) for i in res]


#     with open('result.txt', 'w+') as f:
#         f.write(f'{min(res)}-{max(res)}')
#         f.seek(0)
#         print(f.read())

# with open('result2.txt', 'w+') as file:
#     for i in range(5, 11):
#         file.write(str(i) + '\n')


# with open('result3.txt', 'x') as file:
#     file.write('asdfdsdf')


