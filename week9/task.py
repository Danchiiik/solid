# with open('task1.txt', 'r')as file:
#     print(file.read())
#     file.seek(0)
#     print(file.read())


# with open('task1.txt', 'r')as file:
#     file.seek(0)
#     print(file.readline(1))
#     print(file.readline(2))
#     print(file.tell())


# with open('task2.txt', 'a')as file:
#     for i in range(1, 11):
#         file.write(str(i))
#         file.write('\n')


# with open('task3.txt', 'x')as file:
#     file.write('sadsfgh')




# class A:
#     name = None
    
#     def __init__(self, age) -> None:
#         self.age = age

#     def hello(self):
#         return 'Hello mf'



# class B(A):
    
#     def __init__(self, age, surname) -> None:
#         super().__init__(age)
#         self.surname = surname
    


# obj2 = B(12, 'Sabatarov')
# # obj = A(16)
# # print(obj)
# print(obj2.surname)

# class Math:
#     def __init__(self, value):
#         self.value = value

#     def get_factorial(self):
#         a = 1
#         for i in range(1, self.value+1):
#             a *= i
#         return a
    
#     def get_sum(self):
#         a = str(self.value)
#         b = 0
#         for i in a:
#             b += int(i)
#         return b

#     def get_mul_table(self):
#         a = ''
#         for i in range(1, 11):
#             a += (f'{self.value} x {i} = {self.value*i} \n')
#         return a


# dan = Math(11)
# print(dan.get_factorial())
# print(dan.get_sum())
# print(dan.get_mul_table())



# class Math:
#     def __init__(self, value):
#         self.value = value

#     def get_factorial(self):
#         a = 1
#         for i in range(1, self.value+1):
#             a *= i
#         return a
    
#     def get_sum(self):
#         a = str(self.value)
#         b = 0
#         for i in a:
#             b += int(i)
#         return b

#     def get_mul_table(self):
#         for i in range(0, 11):
#             print(f'{self.value} x {i} = {self.value*i}')

# dan = Math(0)
# print(dan.get_factorial())
# print(dan.get_sum())
# dan.get_mul_table()


# class ToDo:
#     instances = {}

#     def __init__(self, todo):
#         self.todo = todo

#     def give_priority(self, priority):
#         self.priority = priority
#         self.instances[priority] = self.todo
#         return self.instances

#     def list_of_tasks(self):
#         s = []
#         t = list(self.instances)
#         for i in range(1, 4):
#             if i == t[i-1][0]:
#                 s.append(t[i-1])
#         return s

        

# a = ToDo('do homework')
# b = ToDo('watch a film')
# print(b.give_priority(2))
# print(a.give_priority(1))
# print(a.list_of_tasks())




# nums = [1, 1, 1, 2, 2, ]
# b = 0
# a = []
# print(a.pop()) 


n = 19
a = []
for i in str(n):
    a.append(int(i))
while 
