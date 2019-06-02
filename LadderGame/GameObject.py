class GameObject:
    def __init__(self, name, x, y):
        self.name = name # name을 private으로 선언함
        self.coordinate = (x, y) # 위치 좌표를 tuple 형태로 저장함

    def getName(self): # 이름 반환
        return self.name

    def getCoordinate(self): # 현재 위치 좌표를 반환함
        return self.coordinate

    def __str__(self): # 현재 이 객체의 상태를 표시하기 위함
        name = super().__str__()
        return "이름: " + self.name + ", 타입: Person, " + \
               "좌표: (" + str(self.coordinate[0]) + ", " + str(self.coordinate[1]) + ")"

class Person(GameObject): # 사람
    def __init__(self, name, x, y):
        super().__init__(name, x, y)

    def paint(self, canvas): # 사람을 그리는 함수
        canvas.create_text(self.coordinate[0], self.coordinate[1],
                                text=self.name, fill="black")

class Result(GameObject): # 사다리 게임에서 결과에 매칭됨
    def __init__(self, name, x, y):
        super().__init__(name, x, y)

    def paint(self, canvas): # 결과를 그리는 함수
        canvas.create_text(self.coordinate[0], self.coordinate[1],
                                text=self.name, fill="red")