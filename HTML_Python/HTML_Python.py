#coding: utf-8
from tkinter import*
from tk_html_idgets import HTMLLabel

root = Tk ()
root.geometry("700x500")

title = "<h1 style ='color:red;'> Second Pyhton Program </h1>"
subTitle = "<h2 style = 'color:green;> Introduction </h2>"
p = """
<p style ='color:blue;'>
Python is an interpreted, high-level and general-purpose programming 
language. Created by Guido van Rossum and first released in 1991, Python's 
design philosophy emphasizes code readability with its notable use of 
significant whitespace. Its language constructs and object-oriented 
approach aim to help programmers write clear, logical code for small 
and large-scale projects.
</p>
"""
htmlContent = title + subTitle + p 
body = HTMLLabel(root, html = htmlContent)
body.place( x = 20, y = 20, width = 600, height = 500)

root.mainloop()