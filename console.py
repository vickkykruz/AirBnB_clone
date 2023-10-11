#!/usr/bin/python3

"""
    This module contain the implementation of the console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ The command line interpreter """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ End-of-File Marker """
        return True

    def do_exit(self, line):
        """ quits the command line interface """
        return True
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
