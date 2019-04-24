# 리스트 함축
# [출력식 변수의 범위(for i in old_list) 필터(if filter(i))]

S = [x**2 for x in range(10)]
print(S)

M = [x for x in range(10) if x % 2 == 0]
print(M)

list1 = ['all', 'good', 'things', 'must']
items = [word[0] for word in list1] #리스트에서 앞글자만 가져옴
print(items)

word_list = 'doncount your chinckens before they are hatched'.split() #split는 인자가 없으면 스페이스로 자름
result_list = [len(w) for w in word_list] #리스트에서 하나씩 가져와서 길이계산
print(result_list)

colors = ['white', 'red', 'yellow']
cars = ['bmw', 'sonata', 'malibu', 'sm5']
colored_cars = [(x, y) for x in colors for y in cars] #변수의 범위는 튜플을 이용해 x와 y를 정의할 수 있음
print(colored_cars) #상호 곱 수행!