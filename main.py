from tkinter import *
#import tkinter
root= Tk()
#Basic GUI and root is made
#GUI LOGIC
#Width x height

root.geometry(" 4195x61681")
root.minsize("400x400")
# root.maxsize("10000x10000")
#this will lock the max size so you can  not drag the box to increase its size
#the same thing is applicable for minsize
inpt= Label (text="input")
inpt.pack()

root.mainloop()  
