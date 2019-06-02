import tkinter as tk  # GUI
from tkinter import simpledialog
from tkinter import messagebox

import time           # sleep
import sys            # exit
import random as rand # randrange
from LadderGame.GameObject import *

class GameBoard: # 게임 보드 (실제로 보여주는 부분임)
    def __init__(self):
        self.__root = tk.Tk()
        self.__canvas = tk.Canvas(self.__root, width=800, height=350) # 메인 창
        self.__canvas.pack()

        persons_number = self.askInitPersonsNum()
        if persons_number is None:
            sys.exit(1)
        else:
            self.__persons = self.initObjects(persons_number, "User")
            self.__results = self.initObjects(persons_number, "Result")

            for i in range(persons_number):
                self.__persons[i].paint(self.__canvas)
                self.__results[i].paint(self.__canvas)

            self.paintVerticalLines(self.__persons, self.__results) # 세로줄을 먼저 그림

            self.__horizontal_limit = 5    # 가로줄의 한계
            self.__horizontal_info = \
                self.paintHorizontalLines(self.__persons, self.__results, self.__horizontal_limit) # 가로줄을 그림

            self.__horizontal_info.sort()
            print(self.__horizontal_info)

    def askInitPersonsNum(self):
        while True:
            answer = simpledialog.askstring("사람 수 입력", "정수를 입력하세요.", parent=self.__root)
            print(answer)

            if answer is not None:
                if answer.isdigit():
                    result = int(answer)
                    return result
                else:
                    messagebox.showerror("오류", "정수를 입력해야 합니다.")
            else:
                return None

    def initObjects(self, persons_number, type): # type은 User 아니면 Result
        inputDialog = tk.Tk()
        inputDialog.title(type + " 입력")
        inputDialog.geometry("+500+500")
        names = []

        tk.Button(inputDialog, text="OK", command=inputDialog.quit).grid(row=persons_number, column=1)

        entrys = []
        # 이름을 입력받기 위한 라벨 지정
        for row in range(persons_number):
            tk.Label(inputDialog, text=type + " " + str(row + 1) + " Name: ").grid(row=row)
            entry = tk.Entry(inputDialog)
            entry.grid(row=row, column=1)

            entrys.append(entry)

        inputDialog.mainloop()

        # 이름을 리스트에 넣는다
        for row in range(persons_number):
            if entrys[row].get() == "": # 입력하지 않았다면
                names.append(type + " " + str(row + 1)) # 기본 값으로 지정함
            else: # 입력했다면
                names.append(entrys[row].get()) # 입력한 값으로 지정함

        # 객체를 하나씩 추가한다.
        objects = []
        for i in range(persons_number):
            y_coordinate = 0
            if type == "User": # 사용자는 위쪽에 있고
                y_coordinate = 50
            else: # type == Result  -> 결과는 아래쪽에 위치
                y_coordinate = 300

            objects.append(Person(names[i], 50 * (i + 1), y_coordinate)) # x좌표만 10씩 증가
            # print(persons[i])

        inputDialog.destroy()
        return objects

    def paintVerticalLines(self, users, results): # 세로줄을 그림 (인자로는 개수가 넘어옴)
        for i in range(len(users)):
            (startX, startY) = users[i].getCoordinate()
            (endX, endY) = results[i].getCoordinate()

            self.__canvas.create_line(startX, startY + 5, endX, endY - 5, fill="black")

    def paintHorizontalLines(self, users, results, horizontal_limit):
        y_prev = [] # 이전에 그린 가로선에 y좌표를 저장 ->  중복 가로 선을 그릴 수 없게 해야 함 (사다리 게임)
        # tuple 저장 -> (여기서 시작점으로 그리고, 그것에 y좌표)

        for i in range(len(users) - 1): # 5명의 사용자라면, 5개의 라인이 있고, 그 사이는 4개임
            for j in range(horizontal_limit): # 가로선을 그리는 한계까지에 대해서만 반복함
                randNum = -1

                while True: # 무한 루프
                    randNum = rand.randrange(users[0].coordinate[1] + 10, results[0].coordinate[1] - 9)  # a <= x < b
                    if len(y_prev) != 0 and ((i - 1, randNum) in y_prev):
                        # 리스트가 비어있지 않고 만약 그 난수값이 중복된다면
                        continue
                    elif randNum == -1: # 난수 값이 전혀 생성되지 않았다면(즉, 초기화되지 않았다면)
                        continue
                    else:
                        break # 무한 루프 종료

                # 중복되지 않은 난수가 반드시 여기서는 존재함
                y_prev.append((i, randNum)) # 이전에 저장
                self.__canvas.create_line(users[i].coordinate[0], randNum, users[i + 1].coordinate[0], randNum)
                # 가로선을 그림 -> user0 ---- user1

        return y_prev


    def showResult(self): # 결과를 애니메이션으로 보여줌
        oval_size = 10
        oval_radius = oval_size // 2


        print()

        for i in range(len(self.__persons)): # 사람 명수 대로 결과를 보여줘야함
            # 사다리 게임은 수학에서 함수와 마찬가지로, 일대일 대응 함수이다!
            baseX = self.__persons[i].coordinate[0]
            baseY = self.__persons[i].coordinate[1]

            # 원을 그림 -> 이것이 이동할 것임
            current = self.__canvas.create_oval(baseX - oval_radius, baseY - oval_radius,
                                                baseX + oval_radius, baseY + oval_radius,
                                                fill="red")

            current_coordinate = [( (baseX - oval_radius) + (baseX + oval_radius) ) // 2,
                                  ( (baseY - oval_radius) + (baseY + oval_radius) ) // 2]

            current_line = i # 현재 원이 어느 줄에 있는지 확인
            while current_coordinate[1] != self.__results[i].coordinate[1]: # 결과까지 가지 않을 때까지 애니메이션
                print(current_line, current_coordinate)

                if (current_line > 0) and (current_line - 1, current_coordinate[1]) in self.__horizontal_info:
                    # 왼쪽 가로줄을 만나면
                    print("LEFT")

                    current_coordinate[0] -= 1

                    if current_coordinate[0] == self.__persons[current_line - 1].coordinate[0]:
                        print("LEFT -> DOWN")
                        current_line -= 1
                        current_coordinate[1] += 1
                        continue

                    self.__canvas.move(current, -1, 0)
                elif (current_line, current_coordinate[1]) in self.__horizontal_info: # 오른쪽 가로줄을 만나면
                    print("RIGHT")

                    current_coordinate[0] += 1

                    if current_coordinate[0] == self.__persons[current_line + 1].coordinate[0]:
                        print("RIGHT -> DOWN")
                        current_line += 1
                        current_coordinate[1] += 1
                        continue

                    self.__canvas.move(current, 1, 0)
                else: # 세로줄을 만나면
                    print("DOWN")

                    current_coordinate[1] += 1
                    self.__canvas.move(current, 0, 1)

                self.__root.update()
                time.sleep(0.01)


            # 위 while 문을 빠져나오면, 결과는 이미 결정되었다!
            print("RESULTS")

            result_match = ""
            for result in self.__results:
                if (result.coordinate[0], result.coordinate[1]) == \
                    (current_coordinate[0], current_coordinate[1]):
                    result_match = result

            self.__canvas.create_text(result_match.coordinate[0],
                                      result_match.coordinate[1] + 30,
                                      text=self.__persons[i].name)


        self.__root.mainloop()


def main():
    game_board = GameBoard()
    game_board.showResult()


main()