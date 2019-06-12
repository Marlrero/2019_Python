infile = open('proverbs.txt', 'r')

for line in infile:
    line = line.rstrip()
    word_list = line.split() # 공백 문자를 기준으로 분리함
    for word in word_list:
        print(word)

infile.close()