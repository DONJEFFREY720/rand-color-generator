# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 18:30:38 2023

@author: Don Jeffrey
"""
from tkinter import*

import random

root=Tk()
root.title("Title") 
root.geometry("500x500")
root.configure(bg="white")

dictionary = {"color":["red","blue","green","orange","yellow","white","black","purple","darkgoldenrod1","springgreen4","darkorchid1","royalblue","gold","skyblue","slateblue","forestgreen","brown4","seagreen3","deepskyblue2","dodgerblue"]}


def colorChange():
    
    Randno = random.randint(0,len(dictionary["color"])-1)
    path= dictionary["color"][Randno]
    print(Randno)
    root.configure(bg=path)
    print(path)

button = Button(root,text="GENERATE",command=colorChange)

button.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()
