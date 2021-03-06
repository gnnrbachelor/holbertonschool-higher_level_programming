#!/usr/bin/python3
"""Module for base class"""

import json


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string rep of list of dicts"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string rep of list_objs"""
        with open(cls.__name__+'.json', 'w+') as file:
            if list_objs is None:
                file.write("[]")
            else:
                    dict_list = [i.to_dictionary() for i in list_objs]
                    file.write(Base.to_json_string(dict_list))

    def from_json_string(json_string):
        """Returns list from JSON"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instances with all attributes"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                temp = cls(1, 1)
            elif cls.__name__ == "Square":
                temp = cls(1)
            temp.update(**dictionary)
            return temp

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        try:
            with open(cls.__name__+'.json', 'r') as file:
                inst_list = []
                elem = Base.from_json_string(file.read())
                for i in elem:
                    inst_list.append(cls.create(**i))
                return inst_list
        except:
            return []
