# 반복을 이용한 누적은 다른 언어와 표현이 조금 다름

limit = int(input("정수를 입력하시오: "))

# 누적 합
sum = 0
for i in range(1, limit + 1):
    sum += i

print("1부터 %d까지의 정수의 합 = %d" %(limit, sum))

# 팩토리얼
fact = 1.0
for i in range(1, limit + 1):
    fact *= i

print("%d! = %d" %(limit, fact))
