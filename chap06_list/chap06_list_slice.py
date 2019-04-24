# 리스트의 슬라이싱
# list[a:b]에서 [a:b) 구간임

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1[:3]) #[0:3)
print(list1[3:]) #[3:len(list1))
print(list1[:]) #[0:len(list1))

list1[2:5] = ['a', 'b', 'c'] # 대입도 가능!
print(list1)

list1[2:5] = [] #빈 리스트 대입 -> 삭제
print(list1)

# 참고
# list를 뒤에서 추가하려면 append, 특정 인덱스에 추가하려면 insert
# list를 뒤에서 삭제하려면 pop (인자 없음), 특정 인덱스를 삭제하려면 pop (인덱스 인자)
# list에서 어떤 값을 찾아서 삭제하려면 remove(어떤 값)
# list의 길이는 len
# list의 합병은 +, 반복은 *
# list의 요소를 찾으려면 in, 반대는 not in
# list의 비교는 ==, !=, >, < (모든 값과 비교함)
# list의 최댓값은 max, 최솟값은 min으로 찾을 수 있음
# list의 정렬은 list.sort() 혹은 내장함수 sorted(list)를 사용
# list의 정렬에서 key 매개변수를 이용해 요소를 비교하기 전 호출되는 함수 지정 가능
print(sorted("A picture is worth a thousand words.".split(), key=str.lower))
# 역순 정렬
print(sorted([5, 2, 3, 1, 4]))
print(sorted([5, 2, 3, 1, 4], reverse=True))