from tkinter import *

window = Tk()

Label(window, text="aaa", bg="red", fg="white").place(x=0, y=0)
Label(window, text="bbb", bg="green", fg="white").place(x=20, y=20)
Label(window, text="ccc", bg="blue", fg="white").place(x=40, y=40)

window.mainloop()
