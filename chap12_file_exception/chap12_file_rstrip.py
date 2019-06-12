infile = open('proverbs.txt', 'r')
for line in infile:
    line = line.rstrip() # 줄 끝에 줄 바꿈 기호를 삭제
    print(line)
infile.close()