# 알파벳 문자, 숫자, 스페이스의 개수를 세기

string = input("문자열을 입력하시오: ")

alphas = 0 #알파벳 개수
digits = 0 #숫자 개수
spaces = 0 #공백 개수

for char in string:
    if char.isalpha() : #알파벳이면
        alphas += 1
    elif char.isdigit() : #숫자이면
        digits += 1
    elif char.isspace() : #공백이면
        spaces += 1
    else :
        continue

print("알파벳 개수: %d || 숫자 개수: %d || 공백 개수: %d" %(alphas, digits, spaces))