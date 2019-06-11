from tkinter import *

class App: # 클래스를 이용해보자!
    def __init__(self):
        window = Tk() # Root Window
        helloBtn = Button(window, text="Hello", command=self.hello, fg="red")
        # command 인자의 콜백함수는 이 클래스(self)의 hello 함수와 연결됨
        # fg 인자는 foreground -> 텍스트 색을 의미

        helloBtn.pack(side=LEFT)

        quitBtn = Button(window, text="Quit", command=self.quit)
        quitBtn.pack(side=LEFT)

        window.mainloop()

    def hello(self):
        print("Hello 버튼이 클릭됨!")

    def quit(self):
        print("Quit 버튼이 클릭됨!")

App()
# 인스턴스를 생성함