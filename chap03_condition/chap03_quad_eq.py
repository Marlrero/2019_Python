import math

A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

print("식으로 직접 구하기")

D = (B ** 2) - 4 * A * C
if A == 0: #일차 방정식이 됨
    print("x =", -C / B)

if D == 0: #중근
    print("x =", -B / (2.0 * A))
elif D > 0: #실근
    print("x1 =", (-B + math.sqrt(D)) / (2.0 * A))
    print("x2 =", (-B - math.sqrt(D)) / (2.0 * A))
else: #허근
    print("x = 실근이 존재하지 않음")

print("반복해서 구하기")
for x in range(-10000, 10001):
    if A * (x ** 2) + B * x + C == 0:
        print("x = %d" % x)