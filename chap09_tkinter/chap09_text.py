from tkinter import *

window = Tk()
textWidget = Text(window, width=60, height=5)
# width와 height 60 * 5 텍스트 상자 생성

textWidget.pack()
# Pack 배치 관리자

textWidget.insert(END, "테스트 위젯은 여러 줄에 \n 텍스트를 표시할 수 있어요!");
# Text 위젯의 텍스트를 추가함

window.mainloop()