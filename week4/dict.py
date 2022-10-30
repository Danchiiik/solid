# Цикл While (пока)


# age = int(input('Your age mf: '))
# while age <18:
#     age = int(input('Your age mf: '))
# print('Yeah mf, you did it')


# ls = [1, 2, 7, 8]
# while True:
#     print(ls[0])
#     print(ls[1])
#     print(ls[2])
#     print(ls[3])
#     break


# while True:
#     a = int(input('number: '))
#     if a == 5:
#         break
# print('f')


# Тип данных - Словари dict {key = value}
# Это ихменяемый и итерируемый тип данных

# {} - литералы
# синтаксис - {key = value}

# dict_ = {'key1':'value1', 'key2':'value2'}
# print(len(dict_)) #2

# Ключи должны быть уникаьны и неизменяемые, а значение любые

# dict_ = {
#     'name':'John',
#     'age': 22,
#     'hobby' : [
#         'fishing', 'football'
#     ]
# }
# # print(dict_['name'])
# # print(dict_['age'])
# # print(dict_['hobby'][1])
# dict_['age'] = 21
# print(dict_['age'])

# d = {
#     [1, 2, 3]: 'f'
# } # ERROR


# print(dir(dict))


# dict_ = {}
# # print(id(dict_))
# dict_['name'] = 'f'
# dict_[1] = 'first'
# dict_[2] = 'first'
# dict_[2] = 'second'
# # print(id(dict_))
# print(dict_)




#* Методы словарей

# d = {1:1}
# d.clear() #! очищает
# # del d - удаление переменной 
# print(d)


# list_ = [1, 2, 3]
# dict_ = dict.fromkeys(list_)
# dict_ = dict.fromkeys(list_, 'number') #! вставляет в словарь элементы из других данных
# print(dict_)  



# d = {
#     'name':'John' 
#     }
# # print(d['name'])
# print(d.get('name2'))
# print(d.get('name2', 'John is not defined')) #! получить какой то ключ из словаря

# d = {
#     'name':'John',
#     'age': 22
# }
# rem_v = d.pop('age') #! удаление значения
# print(rem_v)

# remoted = d.popitem()
# print(d)
# print(remoted) #! удаляет последний элемент

from codecs import latin_1_decode


d = {
    'name':'John',
    'age':22
}

# age = d.setdefault('age') #! возвращает значение ключа, но если его нет, не создает ошибку, а создает новый ключ со значением None
# age2 = d.setdefault('age2')
# print(age)
# print(age2)
# d.setdefault('age2', 22)
# print(d)

# d2 = {
#     'age':22,
#     'age':23
# }

# d.update(d2)
# d.update({'last_name': 'Show'}) #! обновляет один словарь другим словарем / добавить
# print(d)

# d = {
#     'name':'John',
#     'hello':'world',
#     1:1
# }
# # print(d)
# print(d.items()) #! показывает и значение и ключи
# print(d.values()) #! показывает значение
# print(d.keys()) #!  показывает ключи

# for i in d:
#     print(i)

# for i in d.keys():
#     print(i)

# for i in d.values():
#     print(i)

# for i in d.items():
#     print(i)

# for k, v in d.items():
#     print(f'It is key - {k}, ----- and it is value - {v}')







#! copy vs deepcopy
import copy
l = [1, 2, ['hello']]
# l2 = l
# l2 = l.copy() #* поверхностное копирование
l2 = copy.deepcopy(l)
l2[-1][0] = 'hel'
print(id(l2[-1]))
print(id(l[-1]))
print((l2))
print((l))


