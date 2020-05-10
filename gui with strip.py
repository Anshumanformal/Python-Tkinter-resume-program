from tkinter import *
root = Tk()
root.geometry("744x133")
root.title("My GUI")

f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=BOTTOM, fill="x")

title_label = Label(f2, text ='''Ready''', bg = "red", font="comicsansms 9 bold", borderwidth=3, relief=SUNKEN)
title_label.pack(side=BOTTOM, fill="y", anchor="s")
root.mainloop()