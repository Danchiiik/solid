# [
#     {
#         "id": 1,
#         "name": "Ball",
#         "price": 100.0

#     }
# ]

import json
FILE_PATH = 'data.json'



def get_data(ge_price = None, le_price = None):
    with open(FILE_PATH) as file:
        data = json.load(file)
    if ge_price:
        new_data = [i for i in data if i['price'] >= ge_price]
        return new_data
    if le_price:
        new_data = [i for i in data if i['price'] <= le_price]
        return new_data
    
    return data

    
def get_one_data(id):
    data = get_data()
    one_data = [i for i in data if i['id'] == id]
    if one_data:
        return one_data
    return 'No such data'


def post_data():

    data = get_data()
    try:
        maxid = max([i['id'] for i in data ])
    except ValueError:
        maxid = 0

    data.append({
        'id': maxid + 1,
        'name': input('enter the name: '),
        'price': float(input('enter the price: '))
    })
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
        return 'created'


def update_data(id):
    data = get_data()
    update_d = [i for i in data if i['id'] == id]
    if update_d:
        index_ = data.index(update_d[0])
        data[index_]['name'] = input('enter the new name: ')
        data[index_]['price'] = float(input('enter the new price: '))
        json.dump(data, open(FILE_PATH, 'w'))
        return 'Updated'

    return 'No such data'


def delete_data(id):
    data = get_data()
    delete_d = [i for i in data if i['id'] == id]

    if delete_d:
        data.remove(delete_d[0])
        json.dump(data, open(FILE_PATH, 'w'))
        return 'Deleted'
    return 'No such data'


