from tkinter import *

window = Tk()

scrollbar = Scrollbar(window, orient=VERTICAL) # 스크롤 바를 수직으로 배치
scrollbar.pack(side=RIGHT, fill=Y) # 오른쪽에 배치하고, Y방향으로 채움

listbox = Listbox(window, height=4) # 크기가 4인 리스트 박스 추가
listbox.pack()

scrollbar.configure(command=listbox.yview) # 리스트 박스의 y축에 대해 스크롤바를 등록함
listbox.configure(yscrollcommand=scrollbar.set) # 서로에 대해 알아야 함

listbox.insert(END, 'Python') # 항목 끝(END)에 문자열 추가
listbox.insert(END, 'Java')
listbox.insert(END, 'C')
listbox.insert(END, 'C')
listbox.insert(END, 'C')
listbox.insert(END, 'C')
listbox.insert(END, 'C')
listbox.insert(END, 'C')

window.mainloop()