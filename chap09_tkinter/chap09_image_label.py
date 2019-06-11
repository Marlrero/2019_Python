from tkinter import *

window = Tk()
photo = PhotoImage(file="hello.png")
# 이미지 객체

label = Label(window, image=photo)
# image 매개 변수로 이미지 객체를 넣음

label.pack()
window.mainloop()