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
                data[arg[0] + '.' + new.id] = new
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
                                try:
                                    value = getattr(temp, arg[2])
                                    class_name = eval(value.__class__.__name__)
                                    new_value = class_name(arg[3])
                                    setattr(temp, arg[2], new_value)
                                    data[arg[0] + '.' + arg[1]] = temp
                                except Exception:
                                    my_type = type(arg[2])
                                    setattr(temp, arg[2], my_type(arg[3]))
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

    def do_all_withoutstr(self, arg):
        data = models.storage.all()
        arg = models.sp_quotes(arg)
        length = len(arg)
        if arg[0] in self.classes:
            all_instance = {}
            for id, instance in data.items():
                if id.split('.')[0] == arg[0]:
                    all_instance[id] = instance.to_dict()
            print(all_instance)
        else:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """
        retrieve the number of instances of a class
        """
        count = 0
        data = models.storage.all()
        arg = models.sp_quotes(arg)
        length = len(arg)
        if arg[0] in self.classes:
            for id in data.keys():
                if id.split('.')[0] == arg[0]:
                    count += 1
            print("{:d}".format(count))

    def default(self, line):
        """
        this to custom the point
        where consle will start
            """
        commands = {"all": self.do_all_withoutstr,
                    "show": self.do_show,
                    "count": self.do_count,
                    "destroy": self.do_destroy,
                    "update": self.do_update,
                    "quit": self.do_quit, "EOF": self.do_EOF,
                    "create": self.do_create,
                    "emptyline": self.emptyline, "help": self.do_help}
        for delimiter in ['(', ')', '.', '{', '}', '"', "'", ',', ':']:
            line = " ".join(line.split(delimiter))
            command = line.split()
        if len(command) >= 2:
            if command[1] in commands:
                temp = command[1]
                command[1] = command[0]
                command[0] = temp
                if command[0] == 'all':
                    commands[command[0]](command[1])
                elif command[0] == 'count':
                    commands[command[0]](command[1])
                elif command[0] == 'show':
                    commands[command[0]](command[1] + ' ' + command[2])
                elif command[0] == 'destroy':
                    commands[command[0]](command[1] + ' ' + command[2])
                elif command[0] == 'update':
                    if len(command) > 5:
                        j = 0
                        for i in range(3, len(command)):
                            j += 1
                        x = 3
                        for i in range(0, int(float(j) / 2)):
                            prameter1 = command[1] + ', ' + command[2]
                            prameter2 = command[x] + ', ' + command[x + 1]
                            commands[command[0]](prameter1 + ', ' + prameter2)
                            x = x + 2
                    else:
                        prameter1 = command[1] + ', ' + command[2]
                        prameter2 = command[3] + ', ' + command[4]
                        commands[command[0]](prameter1 + ', ' + prameter2)


if __name__ == '__main__':
    """ should not be executed when imported"""

    HBNBCommand().cmdloop()
