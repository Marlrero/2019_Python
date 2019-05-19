# 하노이 탑 문제도 recursion을 이용하면 편함

# 막대 from에 쌓여있는 n개의 원판을 막대 tmp를 사용해 막대 to로 옮김
def hanoi_tower(n, org, tmp, to):
    if n == 1: # 원판이 1개밖에 없다면
        print("원판 1을", org, "에서", to, "로 옮긴다.") # 종료 조건
    else:
        hanoi_tower(n - 1, org, to, tmp) # from의 맨 밑 원판을 제외한 나머지 원판들을 tmp로 옮김
        print("원판", n, "을", org, "에서", to, "로 옮긴다.") # from에 있는 한 개의 원판을 to로 옮김
        hanoi_tower(n - 1, tmp, org, to) # tmp의 원판들을 to로 옮김

hanoi_tower(4, 'A', 'B', 'C')