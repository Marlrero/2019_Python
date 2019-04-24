# 리스트 클래스를 사용

list1 = list(range(0, 5)) # range함수를 이용
print(list1)

list2 = list("Hello") # 문자열도 시퀀스!
print(list2)

# 리스트의 얕은 복사 문제를 방지하기 위해 사용
list3 = [1, 2, 3, 4, 5]
list4 = list3 #얕은 복사
list3[3] = 'a'
print(list3, list4)

list3 = [1, 2, 3, 4, 5]
list4 = list(list3) #깊은 복사 (list 생성자 이용)
list3[3] = 'a'
print(list3, list4)

from copy import deepcopy
list3 = [1, 2, 3, 4, 5]
list4 = deepcopy(list3) #깊은 복사 (deepcopy 메소드 이용)
list3[3] = 'a'
print(list3, list4)
