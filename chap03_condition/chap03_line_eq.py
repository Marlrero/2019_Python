x1 = int(input("첫 번째 점의 x좌표: "))
y1 = int(input("첫 번째 점의 y좌표: "))
x2 = int(input("두 번째 점의 x좌표: "))
y2 = int(input("두 번째 점의 y좌표: "))

if x2 - x1 != 0 : #분모가 0이 되면 안됨
    slope = (y2 - y1) / (x2 - x1) #기울기 (y = ax + b에서 a)
    y_intercept = y1 - slope * x1 #y절편 (y = ax + b에서 b = y - ax)
    print("직선의 방정식 y = %fx + %f" %(slope, y_intercept))
else:
    print("직선의 방정식 x = %f" %x1)