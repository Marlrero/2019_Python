class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self): # 객체를 문자열로 나타내는 함수
        return "(이름: %s, 나이: %s)" % (self.name, self.age)

def keyAge(person):
    return person.age

people = [
    Person("홍길동", 20),
    Person("김철수", 35),
    Person("최자영", 38)
]

print(sorted(people, key=keyAge)) # 정렬의 기준은 keyAge 함수가 반환하는 값에 의해 결정
print(sorted(people, key=lambda p: p.age)) # 위와 동일한 코드임