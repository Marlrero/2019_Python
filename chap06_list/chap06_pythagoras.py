# 리스트 함축을 이용해 피타고라스 정리를 만족하는 삼각형 찾기

# 원래 코드
new_list = []
for x in range(1, 30):
    for y in range(x, 30): #중복을 제거하려면 x부터 시작!
        for z in range(y, 30): #중복을 제거하려면 y부터 시작!
            if x**2 + y**2 == z**2: #피타고라스 정리
                new_list.append((x, y, z)) #튜플을 리스트에 삽입함

print(new_list)

# 리스트 함축을 이용하면...
print(
    [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30)
     if x**2 + y**2 == z**2]
)