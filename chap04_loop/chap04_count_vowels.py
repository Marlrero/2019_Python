# 자음과 모음의 개수를 세기

origin = input('문자열을 입력하시오: ')
origin = origin.lower() #소문자로 모두 변경함
vowels = 0 #모음
consonants = 0 #자음

if len(origin) > 0 and origin.isalpha(): #문자가 하나라도 있고 알파벳이면
    for char in origin:
        if char in 'aeiou': #모음이면
            vowels += 1
        else : #자음이면
            consonants += 1

print("자음의 개수: %d || 모음의 개수: %d" %(consonants, vowels))