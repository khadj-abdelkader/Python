from tkinter import *
import os

from lib.library import *

root = textEditor("window" , "content")
root.create()
root.add_Text()
root.add_menu()
root.generate()