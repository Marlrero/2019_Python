from tkinter import *

window = Tk()
Label(window, text="Favorite Programming Language").grid(row=0, sticky=W)

list = [ ('Python', IntVar(), 1), ('Java', IntVar(), 2), ('C', IntVar(), 3), ('Swift', IntVar(), 4) ]

for text, value, row in list:
    Checkbutton(window, text=text, variable=value).grid(row=row, sticky=W)
    # sticky가 없으면 중앙정렬이 됨

window.mainloop()