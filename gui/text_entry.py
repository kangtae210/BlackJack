from tkinter import *

root = Tk()
root.title("NADO GUI")
root.geometry("1280x640")


text = Text(root, width = 30, height= 5)
text.pack()

text.insert(END, "글자를 입력하세요")


e = Entry(root, width = 30)
e.pack()
e.insert(0, "한 줄만 입력")

def btncmd():
    print(text.get("1.0", END))         #1번째 라인의 0번째 컬럼부터 끝까지
    print(e.get())

btn = Button(root, text="클릭", command = btncmd)
btn.pack()

root.mainloop()
