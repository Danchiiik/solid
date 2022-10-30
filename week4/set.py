#Set (Множество) это изменяемый, неупор. и итер. тип данных, который хранит в сеье только уникальный згачения, а также хранит в сеье только неиз тип данных.

# - литералы 

# s = {1, 1, 1, 1, 1, 'hello'}
# print(s)

# s = 'abcabcbca'
# l = list(s)
# print(s)

# set_ = set(s)
# print(set_)

# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a.union(b))
# print(a.intersection(b))
# print(dir(set))


# set_ = {1, 2, ('a', 'b')}
# print(set_)


# #! frozenset() 
# b = frozenset()
# print(type(b))
































# admin = {
#     'id': 1,
#     'name': 'John',
#     'password': 'Snow'
# }
# count = 0
# while input() != admin['password']:
#     pass
#     count += 1
#     if count == 3:
#         print('Нурик хватит уже, иди учиться')
#         break
# else:
#     print('Hello')

# a = list(range(1, 101))
# l = []

# for i in a:
#     if i%3 == 0 and i%5 == 0:
#         l.append('FizzBuzz')
#     elif i%3 == 0:
#         l.append('Fizz')
#     elif i%5 == 0:
#         l.append('Buzz')
#     else:
#         l.append(i)
# print(l)