# 난수로 pi의 근삿값을 구해보기
# Monte Carlo 방법: 난수를 수학 문제 해결에 사용함
# 원면적 / 사각형면적 = pi * r^2  /  (2 * r)^2 = pi / 4

# 전체 원을 생각하지 말고, 사분원만을 생각하면 됨! (완벽한 대칭이므로)

# 1. 0.0 ~ 1.0까지의 난수를 발생해 원 안에 떨어지면 inside 변수가 증가함
# 2. 원 안에 떨어졌다는 의미는 원점으로부터 거리가 1.0 이하이어야 함
#    원점으로부터 거리가 1.0이하라는 의미는 원 반지름 범위 안에 있어야 함을 의미
# 3. 전체 점(n)들 중에서 원안에 있는 점(insides)들의 비율 insides/n을 계산한 것이 pi / 4임
# 4. pi = 4 * insides / n

from random import *
from math import sqrt

n = int(input("반복횟수를 입력: ")) #이 횟수가 클수록 점점 더 근사해짐

insides = 0 #사분원 안에 들어오면 증가함
for i in range(0, n): #반복횟수만큼 반복함
    x = random() #[0.0, 1.0) 사이의 난수 발생 (소수)
    y = random()

    if sqrt(x ** 2 + y ** 2) <= 1: #원점으로부터 거리가 1.0(반지름)이하라면
        insides += 1

pi = 4 * insides / n #4분원만 생각했으므로!
print(pi)