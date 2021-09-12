from tkinter import *

root = Tk()
root.title("NADO GUI")
root.geometry("1000x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(END, "사과")
listbox.insert(END, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    #listbox.delete(END)     #마지막항목 삭제
    #print(listbox.size())   #리스트 항목 개수
    #print(listbox.get(0,2))  #리스트의 항목들 가져오기
    #print(listbox.curselection())  #선택항목 반환(위치index로 반환 0,1,2...)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()
