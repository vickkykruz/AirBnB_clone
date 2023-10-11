#!/usr/bin/python3

"""
    This module contains the FileStorage Class
"""
import json
import os


class FileStorage:
    """ This class serializes instances to a JSON file and
        deserializes JSON file to instances

            __file_path: path to the JSON file
            __objects: store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """  sets in __objects the obj with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
        # print(FileStorage.__objects)

    def save(self):
        """ serializes __objects to the JSON file """
        filename = FileStorage.__file_path
        with open(filename, mode="w", encoding="utf8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        filename = FileStorage.__file_path

        if os.path.exists(filename):
            with open(filename, mode="r", encoding="utf8") as f:
                FileStorage.__objects = json.load(f)
        else:
            pass
