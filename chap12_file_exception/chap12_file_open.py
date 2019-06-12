infile = open('phones.txt', 'r', encoding='utf8') # 읽기 모드로 연다. (처음부터 읽기)
str = infile.read(10) # 문자 10개를 읽음
print(str)
infile.close() # 파일 스트림 끊기

print()

infile = open('phones.txt', 'r', encoding='utf8')
line = infile.readline()
while line != "":
    print(line)
    line = infile.readline()
infile.close()