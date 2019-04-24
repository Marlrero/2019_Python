s = input("문자열 입력 >> ")
s = s.replace(" ", "")

if len(s) % 2 == 1:
    if s[0 : len(s) // 2 + 1] == s[len(s) // 2 :][::-1]: #[::-1]을 하는 이유는 reverse!
        print("회문입니다.")
    else:
        print("회문이 아닙니다.")
else:
    if s[0 : len(s) // 2] == s[len(s) // 2 :][::-1]:
        print("회문입니다.")
    else:
        print("회문이 아닙니다.")
