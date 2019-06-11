from tkinter import *
# tkinter 모듈을 포함시킴

window = Tk() # Root Window -> 각 프로그램은 오직 하나의 Root Window를 가져야 함

label = Label(window, text="Hello World!") # Root Window 자식으로 Label 생성
label.pack() # 텍스트를 표시할 정도로 위젯의 크기 축소

window.mainloop() # 윈도우를 닫을 때까지 이벤트 루프에서 대기
# 프로그램이 메인 루프에 진입해야 화면에 윈도우가 나타남