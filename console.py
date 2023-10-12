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
        class_name = args[0]

        for obj_id in stored_objects.keys():
            class_name, unique_id = obj_id.split('.')
            id_list.append(unique_id)
        if args[1] in id_list:
            key = f"{class_name}.{args[1]}"
            obj = stored_objects[key]
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
        except Exception as e:
            pass

        for keys in stored_objects.keys():
            if len(args) < 1:
                all_objects = str(stored_objects[keys])
                instanceList.append(all_objects)
            elif keys.startswith(f"{args[0]}"):
                mySearch = str(stored_objects[keys])
                instanceList.append(mySearch)

        print(instanceList)

    def do_update(self, line):
        """ Updates an instance based on the class name and id
            by adding or updating attribute
        """
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
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")

        stored_objects = FileStorage.all(self)

        class_name = args[0]
        instance_id = args[1]
        att_name = args[2]
        value = args[3].replace("'", '').replace('"', '')

        key = f"{class_name}.{instance_id}"

        if key in stored_objects:
            instance_to_update = stored_objects[key]

        if len(args) >= 3:
            # try:
            #     setattr(key, att_name, value)
            #     FileStorage.save(self)
            # except Exception as e:
            #     print("** no instance found **\n", e)
            setattr(instance_to_update, att_name, value)
            FileStorage.save(self)

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
