# A 사각형을 결정하는 점 P1과 P2
p1x = int(input("첫번째 사각형 P1의 x좌표: "))
p1y = int(input("첫번째 사각형 P1의 y좌표: "))
p2x = int(input("첫번째 사각형 P2의 x좌표: "))
p2y = int(input("첫번째 사각형 P2의 y좌표: "))

# B 사각형을 결정하는 점 P3와 P4가 있을 때,
p3x = int(input("첫번째 사각형 P3의 x좌표: "))
p3y = int(input("첫번째 사각형 P3의 y좌표: "))
p4x = int(input("첫번째 사각형 P4의 x좌표: "))
p4y = int(input("첫번째 사각형 P4의 y좌표: "))

# 2개의 사각형이 겹치지 않는 경우
overlapped = not (p2y < p3y or p2x < p3x or p1y > p4y or p1x > p4x)

if overlapped :
    print("두 개의 사각형이 겹칩니다.")
else :
    print("두 개의 사각형이 겹치지 않습니다.")