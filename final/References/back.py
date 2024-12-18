import os

from References import (loadscreen)


def clean():
    os.system('clear')
clean()

def back():
    global choices
    usr = input("Do you want to continue browsing?? [y/n]: ")
    while True:
        if usr.lower == "n":
            loadscreen
            clean()
    else:
        return()