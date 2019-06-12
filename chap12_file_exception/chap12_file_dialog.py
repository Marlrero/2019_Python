from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

readFile = askopenfilename()
if readFile != None:
    infile = open(readFile, 'r')

for line in infile.readlines(): # readlines는 모든 줄을 가져옴
    line = line.rstrip() # 맨 뒤에 있는 개행 문자 제거
    print(line)

infile.close()