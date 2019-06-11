from tkinter import * # TKinter
import random # 난수 발생

answer = random.randint(1, 100) # [1, 100] 난수 발생

def guessing():
    guess = int(guessField.get()) # Entry 위젯에서 숫자를 가져옴

    # 결과 판단
    if guess > answer:
        msg = "높음"
    elif guess < answer:
        msg = "낮음"
    else:
        msg = "정답"

    resultLabel["text"] = msg # 결과를 출력
    guessField.delete(0, 5) # Entry 위젯을 초기화

def reset(): # 다시 게임 하기
    global answer # 외부 변수
    answer = random.randint(1, 100)
    resultLabel["text"] = "다시 하기!"

window = Tk()
window.configure(bg="white") # Root Window에 대해 배경색 설정
window.title("숫자 맞추기 게임") # Root Window에 대해 제목 설정
window.geometry("500x80") # Root Window에 대해 크기 설정

Label(window, text="숫자 맞추기 게임에 오신 것을 환영합니다~", bg="white").pack()

guessField = Entry(window)
guessField.pack(side=LEFT)

tryButton = Button(window, text="확인", fg="blue", bg="white", command=guessing)
tryButton.pack(side=LEFT)

resetButton = Button(window, text="초기화", fg="red", bg="white", command=reset)
resetButton.pack(side=LEFT)

resultLabel = Label(window, text="1과 100 사이의 숫자를 입력하세요", bg="white")
resultLabel.pack(side=LEFT)

window.mainloop()
