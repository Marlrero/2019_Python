import random

def getPassword():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
              "abcdefghijklmnopqrstuvwxyz" \
              "0123456789" #암호에 들어갈 문자들
    password = "" #결과

    for i in range(6):
        index = random.randrange(len(alphabet)) #알파벳 문자열 크기중에서 하나의 번호를 랜덤하게 선택
        password += alphabet[index]

    #적어도 하나의 숫자가 있는지 확인
    for i in password:
        for ch in "0123456789":
            if i == ch: #숫자를 발견했으면
                return password # 반환

    # 위 return문에 걸리지 않으면 숫자를 발견하지 않은 것임
    number = "0123456789"
    # 주의! 문자열은 변경불가능한 객체임! 인덱스로 대입 불가!
    base = random.randint(0, 5) #임의로 인덱스 선택!
    new_password = password[:base] + number[random.randrange(len(number))] + password[base + 1:]
    #randint는 닫힌구간
    #password에서 임의의 인덱스를 선택해서 숫자를 넣어줌

    return new_password

print(getPassword())
print(getPassword())
print(getPassword())