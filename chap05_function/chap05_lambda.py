# lambda 변수: 변수를 이용한 표현식

L = [lambda x: x**2, lambda x: x**3, lambda x: x**4]

for f in L: #f는 리스트의 원소인 람다식(무명함수이자, 콜백함수)이 넘어옴
    print(f(3)) #3의 제곱, 세제곱, 네제곱을 출력할 것임

min = (lambda x, y: x if x < y else y) #최소값을 반환
                  # 참일때,        거짓일 때

print(min(100, 200))