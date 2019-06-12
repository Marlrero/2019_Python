(x, y) = (2, 0)

try:
    z = x / y # 예외 발생 지점
except ZeroDivisionError as e:
    print(e)