def myGederator():
    yield 'first'
    yield 'second'
    yield 'third'
    # generator은 yield 문장 사용

for word in myGederator():
    print(word)


# chap10_iterator.py와 유사 코드
# Generator는 함수를 이용해 Iterator 객체를 생성하는 것임!
def MyCounterGen(low, high):
    while low <= high:
        yield low
        low += 1

for i in MyCounterGen(1, 10):
    print(i, end=' ')