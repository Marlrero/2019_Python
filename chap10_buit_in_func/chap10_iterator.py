class MyCounter(object):
    # 생성자 메소드 정의
    def __init__(self, low, high):
        self.current = low
        self.high = high

    # iterator -> 객체 자신을 반환
    def __iter__(self):
        return self

    def __next__(self):
        # current가 high보다 크면 StopIteration 예외 발생
        if self.current > self.high:
            raise StopIteration
        else: # high 보다 작으면
            self.current += 1
            return self.current - 1 # 다음 값을 반환함

c = MyCounter(1, 10)
for i in c:
    print(i, end=' ')