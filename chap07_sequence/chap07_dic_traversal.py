# 딕셔너리 순회

scores = { 'korean': 80, 'math': 90, 'english': 80 }
            #key: value

for item in scores: #key가 넘어옴
    print(item, '->', scores[item])

for item in scores.items(): #원소를 튜플로 바꿔줌
    print(item[0], '->', item[1])

print(list(scores)) # key가 넘어옴
print(list(scores.items())) # key-value tuple이 넘어옴
print(list(scores.values())) # value가 넘어옴
# 정렬하고 싶다면, sorted 내장 함수를 사용

for item in scores.values(): #value만 넘어옴
    print(item)

