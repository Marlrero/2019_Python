# 최댓값 구하는 함수 만들기

def max(list):
    max = list[0]
    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]

    return max

print(max([9, 5, 1, 11, 5]))
