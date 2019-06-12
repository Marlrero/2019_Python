def parse_file(path):
    infile = open(path, 'r')

    spaces = 0
    tabs = 0

    for line in infile:
        spaces += line.count(' ') # line에서 count 함수를 이용해 센다
        tabs += line.count('\t')

    infile.close()

    return spaces, tabs

filename = input("파일 이름 입력 >> ")
print("스페이스 수 = %d, 탭의 수 = %d" % (parse_file(filename)))