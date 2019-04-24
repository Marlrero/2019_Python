# 자리수의 합을 출력
number = int(input("정수를 입력하시오: "))

sum = 0
while number > 0:
    digit = number % 10 #맨 밑자리를 뽑아냄
    number = number // 10
    sum += digit

print("자리수의 합:", sum)