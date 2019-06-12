filename = input('파일명 입력: ').strip()
infile = open(filename, 'r')

freqs = {}

for line in infile: # 파일에서 라인을 읽어옴
    for char in line.strip(): # 라인에서 문자 하나씩 가져옴
        if char in freqs:     # 만약 딕셔너리에 문자가 있다면
            freqs[char] += 1  # 1 증가 시킴
        else:
            freqs[char] = 1   # 딕셔너리에 문자를 넣음

print(freqs)
infile.close()