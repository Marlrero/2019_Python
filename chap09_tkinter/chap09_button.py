from tkinter import *

window = Tk()

b1 = Button(window, text="이것이 파이썬 버튼입니다")
b2 = Button(window, text="이것은 두번째 버튼입니다")
# Button의 생성자의 첫 번째 인수는 부모 윈도우. 나머지는 text임

# b1.pack()
# 가장 일반적인 배치 관리자는 pack과 grid임
# pack의 side 인수를 이용해 TOP, BUTTOM, LEFT, RIGHT로 지정 가능
# 기본 값은 TOP임

# b2.pack()
# 기본적으로 pack 배치 관리자는 수직으로 쌓음

# b1.pack(side=LEFT)
# b2.pack(side=LEFT)
# 이렇게 하면 수평으로 배치됨

b1.pack(side=LEFT, padx=10) # padx는 왼쪽과 오른쪽에 10 패딩 추가
b2.pack(side=LEFT, pady=10) # pady는 위쪽과 아래쪽에 10 패딩 추가

b1["text"] = "ONE"
b2["text"] = "TWO"
# text 변경 코드

window.mainloop()