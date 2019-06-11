from tkinter import *

def callback(): # 콜백함수, 핸들러
    button["text"] = "버튼이 클릭~!"

window = Tk()
button = Button(window, text="클릭하세요", command=callback)
# command 인자는 callback 함수와 연결 -> 이벤트 등록

button.pack(side=LEFT)

window.mainloop()