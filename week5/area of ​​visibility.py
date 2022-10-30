
#! Области видимости и пространства имен

#! LEGB - local, enclosed, global, built-in

#! Об. видим. определяет как переменные и имена ищются в вашем коде. Область видимости имен или переменной зависит от того места в коде где вы создаете эту переменную

# x = 'It is global'

# def fun1():
#     x = 'it was local, but now it is enclosed'
#     print(x)
#     def fun2():
#         x = 'it is local'
#         print(x)
#     fun2()

# fun1()
# print(x)



# x = 2

# def f():
#     y = 2
#     print(locals())
# f()
# # print(globals())

# x = 0
# def counter():
#     global x
#     x += 1
#     print(x)
# counter()
# counter()
# counter()

# x = 10
# def f():
#     x = 20
#     print(x)
#     def f2():
#         x = 40
#         print(x)
#     f2()

# print(x)
# f()

def f():
    global y
    y = 2
f()
print(y)

