def getWord(word): #단어인지 검사
    output = str()

    for ch in word:
        if ch.isalpha(): #알파벳이면
            output += ch

    return output.lower() #모두 소문자로 변경해서 리턴

fname = input("파일 이름: ")
file = open(fname, 'r') #파일을 읽기 모드로 열기

result = set() #집합 함수 이용 (집합은 중복은 제거됨)
for line in file: #파일에서 한 라인씩 읽음
    words = line.split() #한 라인을 스페이스로 자름 -> 단어 리스트가 생성됨
    for word in words: # 단어들을 반복해서
        result.add(getWord(word)) #집합에 추가!

print("사용된 단어 >>", result)
