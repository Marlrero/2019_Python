from tkinter import *

window = Tk()
canvas = Canvas(window, width=400, height=300)
canvas.pack()

oval = canvas.create_oval(10, 100, 50, 150, fill="green")

def move_left(event): # 왼쪽으로 5만큼 이동하는 이벤트
    canvas.move(oval, -5, 0)

def move_right(event): # 오른쪽으로 5만큼 이동하는 이벤트
    canvas.move(oval, 5, 0)

canvas.bind_all("<KeyPress-Right>", move_right) # 오른쪽 화살표 키를 누르면 move_right 함수로 바인딩하라
canvas.bind_all("<KeyPress-Left>", move_left)

window.mainloop()