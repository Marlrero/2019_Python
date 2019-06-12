from tkinter import *

file1 = open('hello.png', 'rb')
file2 = open('copy.png', 'wb') # b는 binary를 의미

while True:
    buffer = file1.read(1024) # 1024 bytes 씩 읽음
    if not buffer: # 버퍼가 비면
        break
    file2.write(buffer) # 버퍼만큼 씀

file1.close()
file2.close()
print(file1, '를 ', file2, '로 복사 완료!')

window = Tk()

canvas = Canvas(window, width=300, height=200)
canvas.pack()

image = PhotoImage(file="copy.png")
canvas.create_image(20, 20, anchor=NW, image=image)
# anchor는 이미지의 NW(왼쪽 상단)을 기준점으로 사용하라는 의미

window.mainloop()