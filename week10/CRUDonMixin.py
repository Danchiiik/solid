
#! CRUD на Миксинах

import json
from textwrap import indent
from typing import List

from requests import delete

class ReadDataMixin:
    def read(self, file_name: str) -> list:
        with open(file_name)as file:
            return json.load(file) 


class CreateDataMixin:
    def create(self, file_name:str, data: List[dict], **kwargs:dict) ->None:
        new_id = self.__find__max__id(data)
        data.append({'id': new_id, 
                        **kwargs})
        
        with open(file_name, 'w')as file:
            json.dump(data, file, ensure_ascii=False, indent = 4)

    def __find__max__id(self, data: List[dict]) ->int:
        if data:
            ids = [i['id'] for i in data ]
            return max(ids)+1
        return 0


class UpdateDataMixin:
    def update_data(self, file_name: str, data: List[dict], id: int, **kwargs) -> None:
        for i in data:
            if i['id'] == id:
                i.update(**kwargs)
                break

        with open(file_name, 'w')as file:
            json.dump(data, file, ensure_ascii=False, indent = 4)


class DeleteDataMixin:
    def delete(self, file_name, data, id):
        for i in data:
            if i['id'] == id:
                data.remove(i)
            return 'No such file'

        with open(file_name, 'w')as file:
            json.dump(data, file, ensure_ascii=False, indent = 4)





class ToDo(ReadDataMixin, CreateDataMixin, UpdateDataMixin, DeleteDataMixin):
    def __init__(self, user_name:str) -> None:
        self.user_name = user_name
        self.file_name = user_name + ".json"
        try:
            self.__create_file()
        except FileExistsError:
            print('man, this file is already exist!')

    def __create_file(self):
        with open(self.file_name, 'x') as file:
            json.dump([], file)

john = ToDo('John123')
data_from_file = john.read(john.file_name)
# john.create(file_name=john.file_name, data=data_from_file, title='I need to dance')
# john.update_data(file_name=john.file_name, data=data_from_file, id = 1, forsale = 'Pochka Nurika')
john.delete(file_name=john.file_name, data=data_from_file, id =1)
