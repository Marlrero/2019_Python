try:
    fileName = input('파일명 입력 >> ')
    file = open(fileName, 'r')
except IOError:
    print('파일', fileName, '을 발견할 수 없음!')