import math

choice = int(input("도형을 입력하시오(1: 사각형 면적, 2: 삼각형 면적, 3: 원 면적,"
                   " 4: 원기둥 표면적, 5: 원기둥 부피): "))

if choice == 1 :
    width = int(input("가로: "))
    height = int(input("세로: "))
    print("사각형의 면적:", width * height)
elif choice == 2 :
    base = int(input("밑변: "))
    height = int(input("높이: "))
    print("삼각형의 면적:", 0.5 * base * height)
elif choice == 3 :
    radius = int(input("반지름: "))
    print("원의 면적:", math.pi * radius * radius)
elif choice == 4 :
    radius = int(input("반지름: "))
    height = int(input("높이: "))
    print("원기둥 표면적:", 2 * (math.pi * radius * radius) + (2 * math.pi * radius * height))
elif choice == 5 :
    radius = int(input("반지름: "))
    height = int(input("높이: "))
    print("원기둥 부피:", (math.pi * radius * radius) * height)
else :
    print("잘못 입력하였습니다.")