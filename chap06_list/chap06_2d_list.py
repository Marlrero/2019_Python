# 2차원 리스트(배열)

rows = 3
cols = 5

s = []

for row in range(rows): #행에 대해서
    s += [[0] * cols] # 0 값을 열 갯수만큼 반복해서 1차원 리스트를 만들기!

print(s)

# 리스트 함축을 사용
s = [ ([0] * cols) for row in range(rows) ]
print(s)