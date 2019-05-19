def binarySearch(list, value):          # 선 조건: list는 정렬된 리스트여야 함
    low = 0               # 처음 low는 0이고
    high = len(list) - 1  # 처음 high는 list의 크기 - 1

    while low <= high:    # low가 high을 넘어간다면 탐색은 종료
        middle = (low + high) // 2      # 중간 위치 계산
        if list[middle] > value:        # 중간 위치가 찾을 값보다 더 크다면
            high = middle - 1           # 왼쪽 영역에 있으므로 high를 조정
        elif list[middle] < value:      # 중간 위치가 찾을 값보다 더 작다면
            low = middle + 1            # 오른쪽 영역에 있으므로 low를 조정
        else:
            return middle               # 찾은 경우

    return -1                           # 찾지 못한 경우

myList = [ 2, 6, 11, 13, 18, 20, 22,
           27, 29, 30, 34, 38, 41, 42, 45, 47 ] # 정렬된 리스트에 대해 이진 탐색 수행

print("인덱스=", binarySearch(myList, 34))