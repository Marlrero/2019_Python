def insertionSort(my_list):
    for i in range(1, len(my_list)):
        key = my_list[i] # for문에서 받은 i 위치를 기준으로
        j = i - 1
        while j >= 0 and my_list[j] > key: # key보다 j의 원소가 더 크다면
            my_list[j + 1] = my_list[j]
            j = j - 1                      # j를 1씩 감소시킴 (뒤로 한 칸 씩 가려고)
            my_list[j + 1] = key

my_list = 5, 2, 4, 6, 1, 3]
insertionSort(my_list)
print(my_list)