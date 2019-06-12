def addNumber(fixedNum):
    def add(number):
        return fixedNum + number
    return add # 함수를 반환함
# 고정된 숫자에 전달받은 숫자를 더하는 함수를 반환함

func = addNumber(10)
# 10으로 고정된 숫자로 정의된 함수 func

print(func(20))