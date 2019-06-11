from tkinter import *

window = Tk()
photo = PhotoImage(file="hello.png")

labelImage = Label(window, image=photo).pack(side="right")
# 이미지는 오른쪽에 배치함

labelText = Label(window, text="Hello World!", justify=LEFT, padx=10).pack(side="left")
# 텍스트는 왼쪽 정렬하고 왼쪽과 오른쪽 10 패딩을 주며, 왼쪽에 배치함

window.mainloop()