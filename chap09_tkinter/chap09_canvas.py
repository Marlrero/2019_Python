from tkinter import *

window = Tk()
canvas = Canvas(window, width=300, height=200)
# 캔버스를 생성함

canvas.pack()

canvas.create_line(0, 0, 300, 200)
# 라인을 그림 (0, 0) ~ (300, 200)

canvas.create_line(0, 0, 300, 100, fill="red")
# fill 매개변수는 선 색깔을 의미함

canvas.create_rectangle(50, 25, 200, 100, fill="blue")
# 사각형을 그림. create_line가 매개변수가 비슷함

window.mainloop()