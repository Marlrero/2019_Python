from random import randint

DATA = ["가위", "바위", "보"]
DATA_WIN = {"가위": "바위", "바위": "보", "보": "가위"}
computer = DATA[randint(0, 2)]

try :
    user = input("가위, 바위, 보! >> ")
except ValueError:
    print("안내셨네요~ 졌습니다.")

if computer == user :
    print("비겼습니다!")
elif DATA_WIN[computer] == user :
    print("사용자 승!")
else :
    print("컴퓨터 승!")

print("결과 >> 컴퓨터:", computer, "사용자:", user)
