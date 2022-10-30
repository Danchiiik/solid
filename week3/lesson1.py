# Лекция :
# Python (if). NoneType. Условные операторы

# boolean - неизменимый тип данных

# True - истина
# False - ложь

# print(bool(1))
# print(bool())
# print(bool(""))



# NoneType - ничего

# val = None
# print(type(val))
# print(bool(None))

# print(5 > 2)
# print(5 < 2)
# print(5 >= 2)
# print(5 <= 2)
# print(5 >= 5)

# s = 'hello'
# print('e' in s)
# print('ll' in s)
# print('hl' in s)

#print(True == False and True  == True)

# print(True == True and 5 == 5)

# print(True == True and True == True and False == True)

# print(True or False)
# print(5 > 2 or 5 >6) 
# print(5> 2 or 5 > 3)


# print(not True)
# print(not False)
# print(not False == True and (not True) == (not False))


# Условные операторы (if)
# if 5 > 2:
#     print('Если')
# else:
#     print("Иначе")
# print('Конец')

# a = 2
# b = 3
# if a > b:
#     print('a')
# elif a == b:
#     print("ab")
# else:
#     print("b")


#num = int(input('number 0-5: '))
# if num == 5:
#     print("It is 5")
# elif num == 4:
#     print('It is 4')
# elif num == 3:
#     print('it is 3')
# elif num == 2:
#     print('It is 2')
# elif num == 1:
#     print('It is 1')


# x = 71
# y = -73
# z = -78
# if x < y and z:
#     print(x)
# elif y < x and z:
#     print(y)
# else:
#     print(z)

# x = int(input(" "))
# y = int(input(" "))
# if x%y == 0:
#     print('х делится на у')
#     print("Частное: " + str(x//y))
# else:
#     print('х не делится на у')
#     print("Частное: " + str(x//y))
#     print("Остаток: " + str(x%y))



# s = 'danchik'
# print(s[-2:])

# str = 'abracadabra'
# print(str[0: 6] + 'K' + str[6::])

# age = int(input("How old are you? "))
# name = input("What is your name duuude: ")
# if age >= 18 and name.title() == "Gold" or name.title() == "John Snow":
#     print("Welcome")
# else:
#     print("Лох по жизни, сгинь с глаз моих")
# print(f'Bye {name}')

# Тернарный оператор
# age = 18
# if age == 18:
#     name = "John"
# else:
#     name = "Sam"
# print(name)

# age = 17
# name = "Daniel" if  age == 17 else "Sam"
# print(name)

# num1 = 8
# num2 = 6
# print(num2) if num2 > num1 else print(num1)

# print(max(1, 2, 3, 4))
# print(min(0, -1, 2, 4))
# print(sum([1, 2, 3]))


# print(ord('a'))
# print(ord('h'))
# print(ord('a') + ord('c'))
# print(ord("ss"))

# str = "aha"
# if str == str[::-1]:
#     print("It is polindrol")


#num = 7
#print("четная") if num%2 == 0 else print("нечетное")

#print((1, 2, 3) < (1, 2, 4))

