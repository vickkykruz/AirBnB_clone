#!/usr/bin/python3

"""
    This module contain the implementation of the console
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """ The command line interpreter """

    prompt = "(hbnb) "

    class_list = ["BaseModel"]

    def do_create(self, line):
        """ Creates a new instance of BaseModel """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if line == 'BaseModel':
            new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """ Prints the string representation of an
            instance based on the class name and id
        """
        args = line.split()
        id_list = []

        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing ** ")
            return

        stored_objects = FileStorage.all(self.__dict__)

        for obj_id in stored_objects.keys():
            class_name, unique_id = obj_id.split('.')
            id_list.append(unique_id)
        if args[1] in id_list:
            obj = stored_objects[obj_id]
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing ** ")
            return

        stored_objects = FileStorage.all(self)

        class_name = args[0]
        instance_id = args[1]

        key = f"{class_name}.{instance_id}"

        if key in stored_objects:
            del stored_objects[key]
            FileStorage.save(self)
        else:
            print("** no instance found **")

    def do_all(self, line):
        """ Prints all string representation of
            all instances based or not on the class name.
        """
        instanceList = []
        args = line.split()
        stored_objects = FileStorage.all(self)

        try:
            if args[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")
                return
        except:
            pass

        for keys in stored_objects.keys():
            if len(args) < 1:
                all_objects = str(stored_objects[keys])
                instanceList.append(all_objects)
            elif keys.startswith(f"{args[0]}"):
                mySearch = str(stored_objects[keys])
                instanceList.append(mySearch)

        print(instanceList)

    def do_EOF(self, line):
        """ End-of-File Marker """
        return True

    def emptyline(self):
        return

    def do_exit(self, line):
        """ quits the command line interface """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
