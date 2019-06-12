while True:
    try:
        n = input('숫자 입력 >> ')
        n = int(n) # 예외 발생 지점
        break
    except ValueError:
        print('정수 아님! 다시 입력!')

print('정수 입력 성공!')