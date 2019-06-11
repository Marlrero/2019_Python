from tkinter import *

window = Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()

canvas.create_polygon(10, 10, 150, 110, 250, 20, fill="blue")
# (10, 10) -> (150, 110) -> (250, 20)에 대해 다각형을 파랑색으로 그림
# 좌표들을 모두 리스트에 넣어서 [ 10, 10, 150, 110, 250, 20 ]으로 해도 됨
# outline 매개변수를 사용해도 됨

window.mainloop()