#!/usr/bin/python3
"""created the base class"""
import csv
import json
import os


class Base:
    """Base class for the project defined"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiate the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the string representation of a list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the list of dictionaries to a file"""
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        dicts = cls.to_json_string([i.to_dictionary() for i in list_objs])
        with open(filename, 'w') as f:
            f.write(dicts)

    @staticmethod
    def from_json_string(json_string):
        """converts the json string to dicitonary"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a new instance from the provided dictionary pointer"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns lists of instances of the class"""
        filename = "{}.json".format(cls.__name__)
        list_obj = []
        if not os.path.exists(filename):
            return list_obj
        else:
            with open(filename, 'r')as f:
                tmp = f.read()
                tmp_dict = cls.from_json_string(tmp)
                for i in tmp_dict:
                    list_obj.append(cls.create(**i))
        return list_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects to a file in CSV"""
        csv_file = "{}.csv".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        csv_for = ([i.to_dictionary() for i in list_objs])

        with open(csv_file, 'w', newline='')as csvfile:
            if cls.__name__ == 'Rectangle':
                fields = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == 'Square':
                fields = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(csv_for)

    @classmethod
    def load_from_file_csv(cls):
        """deserilizes the CSV file and returns a list objects involved"""
        file_name = "{}.csv".format(cls.__name__)
        list_obj = []
        if not os.path.exists(file_name):
            return []
        else:
            with open(file_name, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    for key, val in row.items():
                        row[key] = int(val)
                    list_obj.append(cls.create(**row))
        return list_obj
