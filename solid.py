
#? SOLID 

#? SOLID - это абревиатура для набора принципов проектирования, созданная для обьектно-ориентированных языков
#? принципы SOLID направлены для содействия разработки более простого, надежного и обновляемого кода
#? при реализации это делает ваш код более расширяемым, логичным и легким для чтения

# region S



#! S - Single Respubity Principle (принцип единственной обязанности)
# #? Это принцип требует того чтобы один класс выполнял только одну работу (Т. е. не надо создавать огромный класс который делает все)


# # before
# class ExportCsv:
#     def init(self, raw_data):
#       self.data = self.prepare(raw_data)


#     def prepare(self, raw_data):
#       result = ''
#       for item in raw_data:
#           new_line =  f"{item['name']}, {item['surname']}\n"
#           result += new_line
#       return result

        
#     def write_file(self, filename):
#       with open(filename, 'w') as f:
#           f.write(self.data)


# data = [
#   {
#     'name': 'Sherlock',
#     'surname': 'Holmes',
#   },
#   {
#     'name': 'John',
#     'surname': 'Watson',
#   }
# ]

# exporter = ExportCsv(data)
# exporter.write_file('out.csv')

# # after

# class FormatData:
#     def __init__(self, raw_data):
#         self.raw_data = raw_data

    
#     def prepare(self):
#         result = ''
#         for item in self.raw_data:
#             new_line =  f"{item['name']}, {item['surname']}\n"
#             result += new_line
#         return result


# class FileWriter:
#     def init(self, filename):
#         self.filename = filename


#     def write(self, data):
#         with open(self.filename, 'w') as f:
#             f.write(data)


# data = [
#   {
#     'name': 'Sherlock',
#     'surname': 'Holmes'
#   },
#   {
#     'name': 'John',
#     'surname': 'Watson'
#   }
# ]

# formatter = FormatData(data)
# formatted_data = formatter.prepare()

# writer = FileWriter('out.csv')
# writer.write(formatted_data)

# endregion

#! O - Open Closed Principle
# (Принцип  открытости/закрытости)

# Программные сущности (классы, модули, функции) должны быть открыты для расширения, но не для модификации


#* before
# class Discount:
#     def __init__(self, costumer, price) -> None:
#         self.costumer = costumer
#         self.price = price

#     def give_discount(self):
#         if self.costumer == 'o':
#             return self.price *0,2
#         if self.costumer == 'vip':
#             return self.price * 0.4

# obj1 = Discount('o', 20)
# obj2 = Discount('vip', 20)

# #* after
# class Discount:
#     def __init__(self, costumer, price) -> None:
#         self.costumer = costumer
#         self.price = price

#     def give_discount(self):
#         return self.price


# class VIPDiscount(Discount):
#     def give_discount(self):
#         return super().give_discount() *0.4

# class SuperVIPDiscount(Discount):
#     def give_discount(self):
#         return super().give_discount() * 0.8

# obj1 = Discount('o', 20)
# obj2 = Discount('vip', 20)
