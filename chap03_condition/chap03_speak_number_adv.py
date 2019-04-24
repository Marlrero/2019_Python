numbering = ['일', '이', '삼', '사', '오', '육', '칠', '팔', '구']

number = int(input("숫자를 입력하세요: "))

result = ""
if number // 100 > 0:
    result = numbering[number // 100 - 1] + "백 "

if number // 10 > 0:
    result += numbering[(number % 100) // 10 - 1] + "십 "

if number // 1 > 0:
    result += numbering[(number % 10) - 1]

print(result)