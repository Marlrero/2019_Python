from tkinter import *

window = Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()

canvas.create_arc(10, 10, 200, 150, extent=90, style=ARC)
# extent 매개변수는 각도를 지정

window.mainloop()