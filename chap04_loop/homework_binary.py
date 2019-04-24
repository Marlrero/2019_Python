#이진수 변환기

input_number = input("수를 입력하세요 >> ")

#정수부와 소수부를 나누기
pos = input_number.find('.')
if pos != -1 : #소수점을 찾으면
    Z_number, point_number = int(input_number[:pos]), int(input_number[pos+1:])

#print(real_number, point_number)

    
#정수부는 2로 나눈 나머지에 대한 것
ans_Z = ""
if Z_number > 0 : # 양수이면
    while Z_number != 0 :
        ans_Z = str(Z_number % 2) + ans_Z
        Z_number = Z_number // 2
#else : #음수이면 2의 보수로 바꿔라
    

print(ans_Z)

#소수부에 대한 것
ans_P = ""
while point_number != 0 :
    ans_P = str(point_number * 2) + ans_P
    point_number = 1.0 - (point_number * 2) #정수부가 생기면 없애야 함

print(ans_P)
