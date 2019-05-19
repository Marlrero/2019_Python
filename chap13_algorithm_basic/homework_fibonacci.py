# recursion을 이용한 경우
def fib(n):
    if n == 0 or n == 1:
        return n
    else :
        return fib(n - 1) + fib(n - 2)

n = int(input("정수를 입력하시오: "))
print(n, "번째 피보나치 수는", fib(n))

# dynamic programming을 이용한 경우
fiboList = {0: 0, 1: 1} # memo

def fibm(n):
    if not n in fiboList:
        fiboList[n] = fibm(n - 1) + fibm(n - 2)
    return fiboList[n]

n = int(input("정수를 입력하시오: "))
print(n, "번째 피보나치 수는", fibm(n))