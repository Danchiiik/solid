# x = 2
# # x = x + 3
# x += 3
# print(x)

# l = [1]
# l2 = [1]
# print(l ==l2)
# print(id(l))
# print(id(l2))
# print(l is l2)

# a = 2
# b = 2
# print(a is b)

# list_ = ['a', 'b', 'c', 'd']
# # for i in list_:
# #     print(f"под {list_.index(i)} индексом находится - {i}")
# for i in range(len(list_)):
#     print(f'под {i} индексом находится - {list_[i]}')


# d = {'age': 22, 'age': 23}
# print(d['age'])

# l = ['name', 'age']
# d = dict.fromkeys([1, 2, 3], 'aaa')
# print(d

# d = {
#     'John': {
#         'age': 22,
#         'last_name': 'Snow',
#         'weight': 90

#     }
# } 

# print(d['John']['age'])




# for i in range(1, 11):
#     for j in i:
#         print(f'{str(j)} * {str(j)} = {str(j*j)}')


# for i in range(1, 11):
#     for a in range(1, 11):
#         print(f'{i} * {a} = {i*a}')

# d = {'a': 2, 'b':3, 'c': 4}
# d = {i: 'che' if v %2 == 0 else 'neche' for i, v in d.items()}
# print(d)

# d = {'a': {'John':2}, 'c': {'Sam':25}}
# # d = {'a': 2, 'c': 25}

# d = {k: v2 for k, v in d.items() for k2, v2 in v.items()}
# print(d)

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#  'Nik': {'history': 84, 'math': 85, 'literature': 87}}


# d = {k: k2 for k, v in dict_.items() for k2, v2 in v.items() if v2 == max(v.values())}

# print(d)
