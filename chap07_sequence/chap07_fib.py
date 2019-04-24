# 딕셔너리를 이용한 동적프로그래밍 피보나치
table = {0:0, 1:1}

def fib(n):
    if n not in table:
        value = fib(n-1) + fib(n-2) #순환(재귀) 호출
        table[n] = value #호출했던 이전 값을 기억 (동적프로그래밍)

    return table[n]

print(fib(100))