
#! JSON (Java Script Object Notation) - простой формат обмена данными. Людям легко его читать и вести в нем записи, а компьютеры запросто справляются с его синтаксисом. В осносном его применяют для передачи между сервером и веб-приложением (обмен  между backend and frontend)



import json
# data = {'name': 'John', 'age': 22, 'name2': None, 'is_admin': True}
# json_obj = json.dumps(data) # перевели данные в json (Сериализация)
# print(json_obj)

# python_obj = json.loads(json_obj) # перевели json в python (десереализация)
# print(python_obj)



#! Разница типов данных
# Python  JSON
# dict      Object
# list      Array
# tuple      Array
# str      String
# int      Number
# float      Number
# True      true
# False      false
# None      null


# with open('data.json', 'r') as file:
#     # python_data = json.loads(file.read())
#     # print(python_data)
#     python_data = json.load(file)
#     print(python_data)



# Разница между load() и loads(), а также  dump() и dumps() в том что load и dump принимает весь файл и автоматически сер./ дисер. его, а loads  и load  работают со строками.
#? loads, dumps - for string
#? load, dump - for file

# with open('data.json', 'w') as file:
#     json.dump([True, False], file)


