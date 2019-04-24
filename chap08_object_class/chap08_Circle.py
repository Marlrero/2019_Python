import math

#self는 객체 자기 자신이며, 인스턴스 변수 선언시 반드시 self.~
#private으로 정보은닉을 하려면, self.__~해야 하며, 이에 getter와 setter를 해야함!
class Circle:
    def __init__(self, radius=1.0): #생성자 함수로, radius 기본값이 1.0
        self.__radius = radius

    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def calcArea(self):
        return math.pi * (self.__radius ** 2)

    def calCircum(self):
        return 2.0 * math.pi * self.__radius


c1 = Circle(10)
print(c1.getRadius(), c1.calcArea(), c1.calCircum())