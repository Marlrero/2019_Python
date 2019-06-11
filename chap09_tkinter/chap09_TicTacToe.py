from tkinter import *

def checked(i): # i 번째 버튼을 누를 수 있는지 검사함. 누를 수 있으면 O나 X로 표시함
    global player # 외부 변수 player를 사용할 것임
    button = list[i] # 리스트에서 i 번째 버튼 객체를 가져옴

    if button["text"] != "          ": # 버튼이 초기 상태가 아니면 이미 누른 버튼이므로 아무것도 하지 않고 리턴
        return

    button["text"] = "   " + player + "   " # 버튼에 누름

    if player == "X": # X 플레이어가 눌렀으면
        player = "O" # 다음 번에는 O 플레이어가 눌러야 함
        button["bg"] = "yellow"
    else:
        player = "X"
        button["bg"] = "lightgreen"

window = Tk()
player = "X" # 시작 플레이어는 X
list = []

# 9개의 버튼 생성해 격자 형태 배치
for i in range(9):
    btn = Button(window, text="          ", command=lambda k=i: checked(k)) # i번째 버튼에 대해 checked 이벤트 바인딩
    btn.grid(row=i // 3, column=i % 3)
    list.append(btn)

window.mainloop()