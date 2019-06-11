from tkinter import *

def show():
    print("name = %s\n age = %s" % (entryName.get(), entryAge.get()))
    # Entry에서 get 함수를 쓰면 입력한 값을 가져옴

window = Tk()
Label(window, text="name").grid(row=0)
# Grid 배치 관리자를 사용함 -> 행 0번째 붙임

Label(window, text="age").grid(row=1)

entryName = Entry(window)
entryName.grid(row=0, column=1)
# Entry를 생성하고 grid를 같이 써서 entryName에 대입하면 안됨!

entryAge = Entry(window)
entryAge.grid(row=1, column=1)
# 0행 1열에 붙이고, 1행 1열에 붙인 Entry

Button(window, text="show", command=show).grid(row=2, column=0, sticky=W, pady=4)
# sticky는 W(왼쪽)에 붙인다는 의미
Button(window, text="quit", command=window.quit).grid(row=2, column=1, sticky=W, pady=4)
# window.quit 콜백함수는 window를 종료한다는 의미

window.mainloop()