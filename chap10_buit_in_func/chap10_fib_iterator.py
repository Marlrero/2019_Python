class FibIterator:
    # 초기화된 매개변수를 이용함
    def __init__(self, a=1, b=0, maxValue=50):
        self.a = a
        self.b = b
        self.maxValue = maxValue

    # iterator 함수는 객체 자신을 반환함
    def __iter__(self):
        return self

    def __next__(self):
        n = self.a + self.b # 반환할 값
        if n > self.maxValue: # 최댓값보다 크다면
            raise StopIteration # StopIteration 예외를 던짐
        else: # 아니라면
            self.a = self.b # b가 a가 되고
            self.b = n # n이 b가 됨
            return n

for i in FibIterator():
    print(i, end=' ')
