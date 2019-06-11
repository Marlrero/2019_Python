from tkinter import *

window = Tk()

canvas = Canvas(window, width=500, height=200)
canvas.pack()

canvas.create_text(250, 10, text="Hello World!", fill="blue", font="Courier 20")
# font는 ("Courier", 20)으로 해도 됨

canvas.create_text(250, 100, text="Hello World!", fill="red", font="Helvetica 30")

window.mainloop()