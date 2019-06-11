from tkinter import *
import tkinter.font as font

class App:
    def __init__(self):
        window = Tk()

        self.customFont = font.Font(family="Helvetica", size=15) # 직접 Font 객체를 만듬

        label = Label(window, text="Hello World!", font=self.customFont)
        label.pack()

        buttonFrame = Frame(window)
        biggerBtn = Button(buttonFrame, text="+", command=self.biggerText)
        smallerBtn = Button(buttonFrame, text="-", command=self.smallerText)
        biggerBtn.pack()
        smallerBtn.pack()

        buttonFrame.pack()

        window.mainloop()

    def biggerText(self):
        size = self.customFont['size'] # 사이즈를 미리 저장해 놓고
        self.customFont.configure(size=size + 2) # 이 사이즈를 증가 시킴

    def smallerText(self):
        size = self.customFont['size']
        self.customFont.configure(size=size - 2)

App()