from tkinter import *

window = Tk()
label = Label(window, text="Label", font="Helvetica 16")
# font에서 ("Helvetica", 16)으로 해도 됨

label.pack()

window.mainloop()