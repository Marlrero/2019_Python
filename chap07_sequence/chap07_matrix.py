# 희소 행렬을 표현하기 위해 딕셔너리 사용
matrix = {
    (1, 2): 1,
    (2, 2): 2,
    (3, 2): 3
}

for y in range(5):
    for x in range(5):
        print(matrix.get((y, x), 0), end=" ") # get함수는 (y, x)를 가져오는데, 없으면 0을 출력
    print() #개행

