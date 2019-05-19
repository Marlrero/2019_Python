def sequentialSearch(alist, item):
    pos = 0     # 0번째 인덱스로 가정
    found = False

    while pos < len(alist) and not found: # pos는 리스트의 끝까지만, 찾지 못할 때까지만
        if alist[pos] == item:            # 찾았으면
            found = True
        else:                             # 못찾았으면
            pos += 1                      # pos를 1 증가

    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))