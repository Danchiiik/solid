

#!! list comprehension - генереатор списка


# l = []
# for i in range(10):
#     l.append(i)
# print(l)

# l = ['John' for i in range(10)]
# print(str(list(set(l))))


# print('if') if True else print('else')

# l = [i for i in range(10) if i%2 == 0]
# print(l)

# l = [i if i%2 == 0 else 'John' for i in range(10) ]
# print(l)

# l= [i**2 if i%2 == 0 else i**3 for i in range(11)]
# print(l)

# a = {'a': 1, 'b': 2, 'c': 3}
# for i, n in list(a.items()):
#     a[i] = i
#     a[n] = n
# print(a)


# s = 'abcabcabc'
# l = [i for i in s if i == 'a' or i == 'c']
# print(l)


# l = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'john']
# l2 = [i for i in l if 'a' in i]
# print(l2)


#! set comprehension
# l = ['f' for i in range(10)]
# print(l)
# s = {'f' for i in range(10)}
# print(s)





#! dict comprehension
# d = {i:i**2 for i in range(10)}
# print(d)

# d1 = {'a': 5, 'b':4, 'c': 1}
# d = {k:'che' if v%2 == 0 else 'neche' for k, v in d1.items()}
# print(d)

# l = [1, 1, 1, 2, 3, 3, 4]
# d = {i:l.count(i) for i in set(l)}
# print(d)

# l = [True, True, True]
# print(all(l))


# l = [True if i%2 == 0 else False for i in range(10)]
# print(l)


# l = [j for i in range(3) for j in range(i)]
# print(l)


# l1 = {i for i in range(0, 11)}
# print(l1)

l2 = {i:i**2 for i in range(11)}
print(l2)