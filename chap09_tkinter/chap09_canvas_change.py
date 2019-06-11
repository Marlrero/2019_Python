from tkinter import *

window = Tk()

canvas = Canvas(window, width=300, height=200)
canvas.pack()

line = canvas.create_line(0, 0, 300, 200, fill="red")
canvas.coords(line, 0, 0, 300, 100) # line의 좌표를 변경함
canvas.itemconfig(line, fill="blue") # line의 색깔을 변경함

# canvas.delete(line) # line을 삭제함
# canvas.delete(ALL) # 모든 것을 삭제함

window.mainloop()