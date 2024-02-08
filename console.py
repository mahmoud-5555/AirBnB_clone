#!/usr/bin/python3
"""this is the console module"""
import cmd

class HBNBCommand(cmd.Cmd):
    """this simple command processor"""
    def do_greet (self, line):
        print("hello")
    def do_EOF (self, line):
        return True
if(__name__ == 'main'):
    HBNBCommand().cmdloop()