# fibonacci 수열 모듈

def printFib(n): # 수열 출력
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()

def listFib(n): # 리스트 출력
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result