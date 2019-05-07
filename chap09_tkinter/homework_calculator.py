from tkinter import *

def click(key): #클릭할 때 계산하는 이벤트
    if key == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, str(result))
        except:
            entry.delete(0, END) #교재에서 바로 수식 다음에 오류가 떠서 고친 부분
            entry.insert(END, "오류!")
    elif key == 'C':
        entry.delete(0, END)
    else:
        entry.insert(END, key)

window = Tk()
window.title("간단한 계산기")

buttons = [
    '7', '8', '9', '+', 'C',
    '4', '5', '6', '-', ' ',
    '1', '2', '3', '*', ' ',
    '0', '.', '=', '/', ' '
]

#반복문으로 버튼 생성
i = 0
for b in buttons:
    cmd = lambda x = b: click(x) #람다식을 이용해 함수를 정의함
    btn = Button(window, text=b, width=5, relief='ridge', command=cmd) #ridge는 3차원 효과, 이벤트는 cmd
    btn.grid(row=i // 5 + 1, column=i % 5)
    i += 1

#엔트리 위젯은 맨 윗줄의 5개의 셀에 걸쳐서 배치됨
entry = Entry(window, width=33, bg="yellow")
entry.grid(row=0, column=0, columnspan=5) #5개의 셀을 합침

window.mainloop()