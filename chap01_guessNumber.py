number = 62

print("숫자게임에 오신 것을 환영합니다.")

guess = 0
while guess != number:
    guess = int(input("1부터 100 사이의 숫자를 추측해보세요: "))

    if guess < number:
        print("입력한 수보다 작습니다.")
    elif guess > number:
        print("입력한 수보다 큽니다.")
    else:
        print("맞았습니다.")
        break

print("게임이 종료되었습니다.")
