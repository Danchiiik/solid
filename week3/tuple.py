# Кортеж tuple(), цикл for, range

# tuple -> кортеж (неизменяемый, упорядеченный, итерерируемый)

#names = ('John', 'Sam', 'Tolik')
# print(type(names))
# print(names[0])
# #print(dir(names))
# count_name = names.count('John')
# print(count_name)
# print(names.index('Sam'))

#for i in names:
#    print(i)



# Цикл используется в тех случаях, когда нужно повторить что-нибудь Н-ое раз кол. раз или пройтись по итерируемому обьекту


# for i in range(0, 11, 2):
#     print(i)

# l = tuple(range(10))
# print(l)

# l = range(5)
# for i in l:
#     print(i)


# list_ = range(0, 21)
# l1 = []
# l2 = []
# for i in list_:
#     if i%2 == 0:
#         l1.append(i)
#         print(f'{i} - Chetnoe')
#     else:
#         l2.append(i)
#         print(f'{i} - Nechetnoe')
# print(l1)
# print(l2)




################################## break, continue, pass
# pass - заглушка Python 
# break - остановка цикла досрочно
# continue - пропускает код в нужном месте





# for i in range(10):
#     if i == 5 or i == 6:
#         continue
#     print(i)


# for i in range(5):
#     print(i)
#     break
# else: #сработает только тогда когда вышли из цикла без помощи break
#     print('END')


# list_ = ['Alex', 'John', 'Sam', 'Rachel', 'Tolik']
# for i in list_:
#     if i == 'John':
#         continue
#     print(f'Hello! {i}, i want to invite you to party!')

# list_ =[['John', 22], ['Sam', 11], ['Tolik', 45]]
# for i in list_:
#     if i[1] >= 18:
#         print(f'Hello! {i[0]}, come here my friend')
#     else:
#         print(f"{i[0]}, you cant enter, wait {18 - i[1]} years")

# a = len('py')
# print(a)

# for i in range(0, 10):
#     i -= 5
# print(i)

# a = [1, 3]
# print(int(a))








