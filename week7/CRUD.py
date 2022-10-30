
#! CRUD магазина на функциях

# C - create
# R - read
# U - update 
# D - delete

import datetime
data = [
    {
        'id': 1,
        'name': 'product1',
        'price': 100,
        'created_at': datetime.datetime(2022, 10, 4),
        'is_active': True 
    }
]

def get_products():
    return data

def get_one_product(id):
    product = [i for i in data if id == i['id']]
    if product:
        return product[0]
    return 'No such product!'


def post_product():
    max_id = max([i['id'] for i in data ])
    new_data = {
        'id': max_id + 1,
        'name': input('enter the name: '),
        'price': int(input('enter the price: ')),
        'created_at': datetime.datetime.now(),
        'is_active': True
    }
    data.append(new_data)
    return f'You have added {new_data}'


def delete_product(id):
    delete_product = [i for i in data if i['id'] == id]
    if delete_product:
        data.remove(delete_product[0])
        return 'deleted succesfully'
    return 'no such product'


def update_product(id):
    update_product = [i for i in data if i['id'] == id]
    if update_product:
        index_item = data.index(update_product[0])
        
        if input('want to update a name? ') == 'yes':
            data[index_item]['name'] = input('enter a new name: ')
        
        if input('want to update price? ') == 'yes':
            data[index_item]['price'] = int(input('enter a new price: '))
        
        return 'updated succesfully'


    return 'no such product'

def main():
    while True:
        print('hello, there is function:\n 1- get all products,\n 2 - get one product,\n 3 - create product,\n 4 - delete product,\n 5 - update product,\n 0 - to exit ')
        method = input('enter the number: ')
        if method == '1':
            print(get_products())
            print('\n')
        elif method == '2':
            id = int(input('enter the id: '))
            print(get_one_product(id))
            print('\n')
        elif method == '3':
            print(post_product())
            print('\n')
        elif method == '4':
            id = int(input('enter the id: '))
            print(delete_product(id))
            print('\n')
        elif method == '5':
            id = int(input('enter the id: '))
            print(update_product(id))
            print('\n')
        elif method == '0':
            break
        else:
            print('no such method')



if __name__ == '__main__':
    main()