file = open('data.csv', 'r')

for line in file.readlines(): # 라인 전체 가져오기
    line = line.strip() # 공백/개행을 없앰

    print(line) # 줄 출력
    parts = line.split(',') # 콤마 분리

    for part in parts: # 콤마 단위로 분리된 각각에 대해
        print("\t", part)

file.close()