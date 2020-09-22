# coding: utf-8
from tkinter import *
import os

class textEditor
	def__init__(self, master, content):
	self.master = master
	self.content = content

#-------------------
# Main window creation
#-------------------
	def create(self):
	self.master = Tk()
	self.master.title("Text Editor")
	self.master.geometry("700*400") 
	def add_text(self):
	self.content = Text(self.master)
	self.content.pack(expand = True, fill = 'both')

	def generate(self):
	self.master.mainloop()
#--------------------
# Menu creation
#--------------------
	def quit(self):
		self.master.quit()
	def add_menu(self):	
		menuBar = Menu(self.master)
		Filemenu = Menu(menuBar, tearoff = False)
		menuBar.add_cascade(label = "File", menu = Filemenu)
		Filemenu.add_command(label = "Quit", command = self.quit)
		self.master.config(menu = menuBar)


