#!/usr/bin/python3
"""this is the console module"""
import cmd

class HBNBCommand(cmd.Cmd):
    """this simple command processor"""
    prompt = '(hbnb) '
    def do_quit (self, line):
        """ Quit command to exit the program"""
        return True
    def do_EOF (self, line):
        """ EOF command to exit the program"""
        return True
    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass
    def do_help(self, arg):
        """print newline after help commands"""
        cmd.Cmd.do_help(self, arg)
        if arg:
            print()
    
if(__name__ == '__main__'):
    """ should not be executed when imported"""
    HBNBCommand().cmdloop()