file = open('proverbs.txt', 'r+')
str = file.read(10)
print('읽은 문자열 >>', str)
pos = file.tell() # 현재 읽은 위치
print('현재 위치 >>', pos)

pos = file.seek(0, 0) # 파일의 처음으로 이동
str = file.read(10)
print('다시 읽은 문자열 >>', str)

file.close()