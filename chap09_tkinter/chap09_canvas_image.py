from tkinter import *

window = Tk()

canvas = Canvas(window, width=300, height=200)
canvas.pack()

image = PhotoImage(file="hello.png")
canvas.create_image(20, 20, anchor=NW, image=image)
# anchor는 이미지의 NW(왼쪽 상단)을 기준점으로 사용하라는 의미

window.mainloop()