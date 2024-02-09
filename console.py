#!/usr/bin/python3
"""this is the console module"""
import cmd
from models.base_model import BaseModel
import models
import json
import re


class HBNBCommand(cmd.Cmd):
    """this simple command processor"""
    prompt = '(hbnb) '

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

    def do_create(self, obj_name):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not obj_name:
            print("** class name missing **")
        elif obj_name != 'BaseModel':
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        classes = ['BaseModel']
        data = models.storage.all()
        arg = models.sp_quotes(arg)
        length = len(arg)
        if length > 0:
            if arg[0] in classes:
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
        classes = ['BaseModel']
        data = models.storage.all()
        arg = models.sp_quotes(arg)
        length = len(arg)
        if length > 0:
            if arg[0] in classes:
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
        classes = ['BaseModel']
        data = models.storage.all()
        arg = models.sp_quotes(arg)
        length = len(arg)
        if length == 0:
            all_instance = []
            for instance in data.values():
                all_instance.append(str(instance))
            print(all_instance)
        else:
            if arg[0] in classes:
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
        classes = ['BaseModel']
        data = models.storage.all()
        arg = models.sp_quotes(arg)
        length = len(arg)
        if length > 0:
            if arg[0] in classes:
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


if(__name__ == '__main__'):
    """ should not be executed when imported"""

    HBNBCommand().cmdloop()
