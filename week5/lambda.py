
#! Lambda - это анонимная функция которая имеет более краткую запись и чаще всего вызывается только один раз

# lambda arguments: expression - синтаксис

# def get_sum(a, b):
#     return a+b
# a = get_sum
# print(a(1, 2))



# f = lambda a, b: a+b
# print(f('fgfg', 'dgfg'))


# f = lambda x: print(x)
# print(f(5))

# d = lambda a, b, c: (a+b)*c
# print(d(1, 2, 3))

#! split and join

# s= 'hello john snow'
# l = s.split(' ')
# print(l)

# l = ['hello', 'john', 'snow']
# s = ' '.join(l)
# print(s)

#! sort() and sorted()

# print(dir(list)) # sort()

# l = ['asds', 'aa', 'b', 'fff']
# # l.sort(reverse=True)
# l.sort(key = len, reverse=True)
# print(l)


# l = ['a', 2, 3]
# l.sort()
# print(l)


# s = 'erghjhgbvfcdsx'
# s2 = sorted(s, reverse=True)
# print(s2)

# d = ''.join(s2)
# print(d)

#! Константа Const
# AGE = 123

import random
# l = ['a', 'v', 'c']
# ans = random.choice(l)
# print(ans)

# print(random.randint(0, 100))

# def f():
#     global x
#     x = 100
# f()
# print(x)

# x = 100

# def f():
#     x = 30
#     print(id(x))
# print(id(x))
# f()

# x = 10

# def f1():
#     x = 20
#     print(x)
#     def f2():
#         nonlocal x
#         print(x)
#         x = 30
#         print(x)
#     f2()
# f1()

# print(x)
# print(globals())


# l = [ord(str(i)) for i in range(10)]
# print(l)

# import time
# import datetime

# # for i in range(10):
# #     print(i)
# #     time.sleep(10)

# print(datetime.datetime.now())def summ(x):
#     # res = 0
#     # for i in str(x):
#     #     res += int(i)
#     return sum([int(i) for i in str(x)]) 
# print(summ(333))


# def summ(x):
#     # res = 0
#     # for i in str(x):
#     #     res += int(i)
#     return sum([int(i) for i in str(x)]) 
# print(summ(333))

# clients = [('Jack', 25), ('Helen', 18), ('Mike', 15), ('Jessica', 32), ('Jack', 25), ('Alice', 28), ('Mike', 15)]
# for i in set(clients):
#     if i[1] >= 18:
#         print(f'Здравствуй {i[0]}. У нас скидка на алкоголь')
#     else:
#         print(f'Здравствуй {i[0]}, с новым годом!')

# import random
# friends= ['Elida', 'Nurik', 'Adelya', 'Azim', 'Slava', 'Alice']
# gift = [['Harry Potter', 'It', 'Rich&Poor Dad'],  
#         ['Samsung Phone', 'Xiaomi Phone', 'Pochka Nurika'],
#         ['20% Tucci discount', '10%e LV discount', '15% Apple discount']]

# # for i in fr:
# #     for j in random.choice(gift):
# #         print(j)
# #     #     fgift = random.choice(j)
# #     # print(f'{i} -> {fgift}')

# all_present = [*gift[0], *gift[1], *gift[2]]
# random.shuffle(all_present)

# for name in friends:
#     print(f'{name}  --->  {all_present.pop()}')

a = 'уеыаоэяию'
b = 'йцкнгшщзхфвпрлджчсмт'
def count_symbols(x):
    global a
    f = 0
    g = 0
    l = 0
    for i in x:
        if i in a:
            f +=1
        elif i in b:
            g +=1
        else:
            l += 1
    return f'Количество гласных: {f}, согласных: {g}, остальных символов: {l} '

print(count_symbols('Мурат супер!'))

