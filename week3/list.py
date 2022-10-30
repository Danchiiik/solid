# list = []
# list = [1, True, [1, 2, 3 ], 'hello']
# list[-1] = 'Danchik'
# print(list)

# list = [1, 2, 3, 4, 5]
# list2 = [1, 2, 3, 4, 5]
# print( list == list2)

# a = [1, 2, True]
# print(type(a))











# Методы списков
# append() -> добавляет элементы в список
# range(start, end, step) -> генерация
# extend(list) -> расширение листа, добавление элемента в конец
# insert(in, el) -> добавляет элемент в указанный индекс
# remove() -> удаление. только 1 элемент
# pop(in) -> удаление по индексу. Возвращает уд. элемент.
# index(el, start, end) -> находит индекс элемента  
# count(el) -> возвращает N кол. элемента 
# sort(reverse = True, key = function) -> сортирует список на основе функции
# ' '.join(list) -> из листа делает строку
# copy -> поверхносное копирование
# clear() -> очистка






# list = []
# inp = input('Enter value: ')
# list.append(inp)
# print(list2)


# range(start, end, step)
# ls = list(range(0, 11, 2))
# print(ls)

# list = [1, 3, True, 9, False]
# for i in list:
#     print(i)

# ls = []
# for i in range(11):
#     ls.append(i)
#     print(i)
# print(ls)

# ls = [1, 'hello']
# ls2 = [2, 3, 45, 1, 34]

# ls.extend(['makers', 3, 5])
# print(ls)
# print(ls2)
# print(sorted(ls2))

# print(sorted([7, 5]*2)

# ls = [1, 3, 4, 5]
# ls.insert(1, 'makers')
# print(ls)

# a = ls(1).replace('makers', 'Danchik')
# print(a)

# a = 'makers'
# b = a.replace('makers', 'Danchik')
# print(b)

# l = [[1, 2, 3], [5, 6, 7]]
# l[0][1] = 100
# print(l)


# l = ['h', 'g', 2, 'k',  2, 'e', 8]
# l.remove('h')
# print(l)

# ls = []
# for i in l:
#     if type(i) == str:
#         ls.append(i)
# print(ls)


# ls = [1, 2, 3, 4, 5, 6, 'g', 'h', 'd', ]
# a = ls.pop(0)
# print(a)
# print(ls)


# ls = [2, 4, 5, 67, 300, 3, 78, 2, 3, 45, 65, 300]
# print(ls.index(300))


# ls = ['h', 'e', 'l', 'l']
# print(ls.count('l'))

# ls = [5, 6, 9, 1, 3, 90]
# ls.sort()
# print(ls)

# ls = ['a', 'f', 'fg', 'thy', 'd']
# # ls.sort(key=len)
# # print(ls)

# ls.sort(reverse=True, key=len)
# print(ls)

# ls = [3, 5, 7, 9, 133]
# ls.reverse()
# print(ls)


# a = input("aaa: ")
# f = a.split()
# print(f)

# ls = ['heart', 'of', 'Nurik']
# a = ' '.join(ls)
# print(a)


# ls = [1, 2, 3, 4, 5]
# ls2 = ls.copy()
# ls2.append(45)
# print(ls)
# print(ls2)

# import copy
# ls = [1, 3, 5, [1, 3, 6, 8]]
# ls2 = copy.deepcopy(ls)
# ls2[-1].append(9)
# print(ls)
# print(ls2)

# ls = [2, 3, 4, 5,]
# print(ls)
# ls.clear()
# print(ls, 'list cleared')

# s = ["danchik"]
# d  = list(s[0])
# a = d[len(d)//2]
# print(a)

# list_ = ['Nurik', 'pochka']
# list_.reverse()
# print(list_)

# list_ = input()
# list_.split(',')
# print(sorted(list_))

# inp1 = input()

# list_ = inp1.split(',')
# list_ = sorted(list_)

# print(list_)

a = input()
list_ = a.split(',')
print(sorted(list_))
