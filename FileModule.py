import os
from tkinter import filedialog
from tkinter import *

# Types of opening file:
# A - Append (Write without overwriting)
# W - Write (Overwrites the file)
# R - Read (Outputs the read file as a string)
# X - Create (Creates a file with the name

def OpenFile(name, typeof):
    return open(name, typeof)
def CloseFile(file):
    file.close()
def WriteFile(file, text):
    file.write(text)
def ReadFile(name):
    file = open(name, "r")
    return(file.read())
def DeleteFile(name):
    os.remove(name)
def DoesExist(name):
    if os.path.exists(name):
        return True
    return False
def DeleteFolder(name):
    os.rmdir(name)
def AskOpenFile():
    return filedialog.askopenfilename(initialdir=os.getcwd(),title="Open",filetypes=(("Text File", "*.txt"), ("All Files","*.*")))
def AskSaveFile():
    files = [("Text Document", "*.txt")]
    return filedialog.asksaveasfile(filetypes=files,defaultextension=files)


