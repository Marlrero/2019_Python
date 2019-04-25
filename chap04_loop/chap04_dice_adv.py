# 주사위 2개를 던졌을 때, 합이 6이 되는 경우를 출력
print([(x, y) for x in range(1, 7) for y in range(1, 7) if x + y == 6])

# 주사위 3개를 던졌을 때, 합이 10이 되는 경우를 출력
print([(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7) if x + y + z == 10])