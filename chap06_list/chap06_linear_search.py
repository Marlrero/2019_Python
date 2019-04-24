# 선형 탐색 알고리즘

def linearSearch(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i #위치 반환

    return -1 #못찾을 때 반환

print(linearSearch([9, 8, 7, 5], 5))
print(linearSearch([9, 8, 7, 5], 1))

# 이 외에도 정렬 알고리즘도 구현가능!