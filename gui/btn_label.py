from tkinter import *

root = Tk()
root.title("NADO GUI")
root.geometry("1280x640")
# root.resizable(False, False)    #너비, 높이 값 변경 불가능
    
def btn1_press():
    label1.config(text="label1이 바뀜")
    print("label1이 바뀜")

btn1 = Button(root, text="버튼1", command=btn1_press)
btn1.pack()

label1 = Label(root, text ="안녕하세요")
label1.pack()

root.mainloop()










