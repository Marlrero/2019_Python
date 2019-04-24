# 2개의 주사위를 던져 나오는 합의 확률

from random import randint #random에서 randint만 사용!

count = int(input('주사위 실험 반복횟수: '))
rollCount = [0, 0, 0, 0, 0,
             0, 0, 0, 0, 0,
             0, 0, 0] #0과 1은 사용하지 않음 (2개의 주사위를 던지면 합의 최솟값이 2)

for i in range(count): #입력값 만큼 반복
    die1 = randint(1, 6) # 닫힌구간 [1, 6] 난수 발생
    die2 = randint(1, 6)
    rollCount[die1 + die2] += 1 #주목!

for i in range(2, 13): #rollCount에서 0, 1번 인덱스는 제외
    print(i, '->', rollCount[i])