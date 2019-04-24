# 난수 생성을 이용해서 chap01_guessNumber를 바꿔보자!
import random

number = random.randint(1, 100) #이 부분이 바뀜! (1 ~ 99값의 난수)

print("숫자게임에 오신 것을 환영합니다.")

guess = 0
while guess != number: # 이 부분을 따로 if break로 걸고, tries(시도 횟수)로 할 수도 있음
    guess = int(input("1부터 100 사이의 숫자를 추측해보세요: "))

    if guess < number:
        print("입력한 수보다 작습니다.")
    elif guess > number:
        print("입력한 수보다 큽니다.")
    else:
        print("맞았습니다.")
        break

print("게임이 종료되었습니다.")