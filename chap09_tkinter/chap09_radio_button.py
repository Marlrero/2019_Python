from tkinter import *

window = Tk()
choice = IntVar() # 정수형 변수를 생성하여, 라디오 버튼 4개와 연관시키게 함

Label(window, text="Favorite Programming Language", justify=LEFT, padx=20).pack()

'''
Radiobutton(window, text="Python", padx=20, variable=choice, value=1).pack(anchor=W)
# variable 매개변수는 다른 라디오버튼과 연관되게 하는 것이고, value는 그 값을 말함
# anchor를 이용해 왼쪽(W)에 붙임(pack)

Radiobutton(window, text="Java", padx=20, variable=choice, value=2).pack(anchor=W)

Radiobutton(window, text="C", padx=20, variable=choice, value=3).pack(anchor=W)

Radiobutton(window, text="Swift", padx=20, variable=choice, value=4).pack(anchor=W)
'''

# 위 주석을 아래와 같이 쓸 수 있음

list = [ ('Python', 1), ('Java', 2), ('C', 3), ('Swift', 4) ]

choice.set(1) # 기본 선택 값을 줄 수도 있음

def printChoice():
    print(choice.get()) # 선택할 때마다 값이 출력될 것임

for txt, val in list: # 튜플이 넘어오므로 두 개의 변수를 선언
    Radiobutton(window, text=txt, padx=20, variable=choice, command=printChoice, value=val).pack(anchor=W)
    # command 매개변수로 앞서 정의한 printChoice 함수를 콜백함수로 지정

window.mainloop()