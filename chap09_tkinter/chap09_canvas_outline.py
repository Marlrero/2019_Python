from tkinter import *

window = Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()

canvas.create_rectangle(50, 25, 200, 100, outline="blue")
# outline은 바깥선 색깔을 변경하는 것임
# 색깔은 #16진수를 이용해도 됨

window.mainloop()