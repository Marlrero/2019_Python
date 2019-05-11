class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return "\n이름=" + self.name + "\n주민번호=" + self.number

class Student(Person):
    # 상수
    UNDERGRADUATE = 0
    POSTGRADUATE = 1

    def __init__(self, name, number, studentType):
        super().__init__(name, number)
        self.studentType = studentType
        self.gpa = 0
        self.classes = []

    def enrollCourse(self, course):
        self.classes.append(course)

    def __str__(self):
        return super().__str__() + "\n수강과목=" + str(self.classes) +\
            "\n평점=" + str(self.gpa)

class Teacher(Person):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.courses = []
        self.salary = 3000000

    def assginTeaching(self, course):
        self.courses.append(course)

    def __str__(self):
        return super().__str__() + "\n강의과목=" + str(self.courses) +\
            "\n월급=" + str(self.salary)

hong = Student("홍길동", "12345678", Student.UNDERGRADUATE)
hong.enrollCourse("자료구조")
print(hong)

kim = Teacher("김철수", "1234567890")
kim.assginTeaching("Python")
print(kim)