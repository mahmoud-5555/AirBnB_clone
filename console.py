#!/usr/bin/python3
"""this is the console module"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import json
import re


class HBNBCommand(cmd.Cmd):
    """this simple command processor"""
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'State',
               'City',  'Amenity', 'Place', 'Review']

    def do_quit(self, line):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """ EOF command to exit the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_help(self, arg):
        """print newline after help commands"""
        cmd.Cmd.do_help(self, arg)
        print()

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        arg = models.sp_quotes(arg)
        data = models.storage.all()
        if len(arg) > 0:
            if arg[0] in self.classes:
                new = eval(arg[0])()
                data[arg[0]+ '.' + new.id] = new
                models.storage.__objects = data
                models.storage.save()
                print(new.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id
        """

        data = models.storage.all()
        arg = models.sp_quotes(arg)
        length = len(arg)
        if length > 0:
            if arg[0] in self.classes:
                if length > 1:
                    if arg[0] + '.' + arg[1] in data.keys():
                        print(data[arg[0] + '.' + arg[1]])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        destroy the string representation of an
        instance based on the class name and id
        """
        data = models.storage.all()
        arg = models.sp_quotes(arg)
        length = len(arg)
        if length > 0:
            if arg[0] in self.classes:
                if length > 1:
                    if arg[0] + '.' + arg[1] in data.keys():
                        del data[arg[0] + '.' + arg[1]]
                        models.storage.__objects = data
                        models.storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        data = models.storage.all()
        arg = models.sp_quotes(arg)
        length = len(arg)
        if length == 0:
            all_instance = []
            for instance in data.values():
                all_instance.append(str(instance))
            print(all_instance)
        else:
            if arg[0] in self.classes:
                all_instance = []
                for id in data.keys():
                    if id.split('.')[0] == arg[0]:
                        all_instance.append(str(data[id]))
                print(all_instance)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        data = models.storage.all()
        arg = models.sp_quotes(arg)
        length = len(arg)
        if length > 0:
            if arg[0] in self.classes:
                if length > 1:
                    if arg[0] + '.' + arg[1] in data.keys():
                        if length > 2:
                            if length > 3:
                                temp = data[arg[0] + '.' + arg[1]]
                                value = getattr(temp, arg[2])
                                class_name = eval(value.__class__.__name__)
                                new_value = class_name(arg[3])
                                setattr(temp, arg[2], new_value)
                                data[arg[0] + '.' + arg[1]] = temp
                                models.storage.__objects = data
                                models.storage.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    """ should not be executed when imported"""

    HBNBCommand().cmdloop()
