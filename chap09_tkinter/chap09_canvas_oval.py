from tkinter import *

window =  Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()

canvas.create_oval(10, 10, 200, 150)
# 타원도 사각형 그리는 것과 마찬가지임

window.mainloop()