def getMinPos(alist, start): # 최솟값의 위치를 반환
    minPos = start     # 처음 위치로 가정함
    for i in range(start + 1, len(alist)): # 시작 위치부터 리스트에 끝까지에 대해
        if alist[i] < alist[minPos]:       # i 위치가 더 작다면
            minPos = i                     # i 위치가 제일 작은 곳임

    return minPos

def selectionSort(alist):    # 실제 정렬이 수행됨
    for i in range(len(alist)):
        minPos = getMinPos(alist, i)
        temp = alist[minPos]
        alist[minPos] = alist[i]
        alist[i] = temp

alist = [1, 4, 5, 9, 8, 2, 7]
selectionSort(alist)
print(alist)