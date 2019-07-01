#!/usr/bin/python3
""" Cmd line entry point """
import cmd
import models
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """ Cmd line interpreter """
    prompt = "(hbnb) "

    def emptyline(self):
        """ empty implementation """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    do_EOF = do_quit

    def do_create(self, args=None):
        """Creates a new instance of BaseModel, s
        aves it (to the JSON file) and prints the id"""
        try:
            if not args:
                print("** class name missing **")
            else:
                newinstance = args.split()
                newinstance = eval(args)()
                newinstance.save()
                print(newinstance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args=None):
        """Prints the string representation of an instance based
        on the class name and id. Ex: $ show BaseModel 1234-1234-1234"""
        try:
            line = args.split()
            if len(line) == 0:
                print("** class name missing **")
            elif len(line) == 1:
                print("** instance id missing **")
            else:
                instance = line[0] + "." + line[1]
                if instance in models.storage.all():
                    print(models.storage.all()[instance])
                else:
                    print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, args=None):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        try:
            line = args.split()
            if len(line) == 0:
                print("** class name missing **")
            elif len(line) == 1:
                print("** instance id missing **")
            else:
                instance = line[0] + "." + line[1]
                if instance in models.storage.all():
                    del models.storage.all()[instance]
                    models.storage.save()
                else:
                    print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, args=None):
        """Prints all string representation of all instances
        based or not on the class name"""
        try:
            line = args.split()
            temp = []
            for key in models.storage.all():
                v = models.storage.all()[key]
                classname = key.split(".")
                if classname[0] == args or len(args) == 0:
                    temp.append(str(v))
                    print(temp)
                else:
                    print("** class doesn't exist **")
        except NameError:
            print("** class doesn't exist **")

    def _int(self, stri):
        try:
            int(stri)
            return True
        except ValueError:
            return False

    def _float(self, stri):
        try:
            float(stri)
            return True
        except ValueError:
            return False

    def do_update(self, args=None):
        """ Updates an instance based on the class na-
        me and id by adding or updating attribute
        (save the change into the JSON file)."""
        try:
            argz = args.split()
            if len(argz) == 0:
                print("** class name missing **")
            elif len(argz) == 1:
                print("** instance id missing **")
            elif len(argz) == 2:
                print("** attribute name missing **")
            elif len(argz) == 3:
                print("** value missing **")
            else:
                objs = argz[0] + "." + argz[1]
                if objs in models.storage.all():
                    if self._int(argz[3]):
                        argz[3] = int(argz[3])
                    elif self._float(argz[3]):
                        argz[3] = float(argz[3])
                    if type(argz[3]) == str:
                        argz[3] = argz[3][1:-1]
                    setattr(models.storage.all()[objs], argz[2], argz[3])
                else:
                    print("** no instance found **")
        except ValueError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
