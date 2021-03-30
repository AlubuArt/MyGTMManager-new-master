from tkinter import *


root = Tk()
frame = Frame(root, height=400, width=400)
frame.pack()

topFrame = Frame()
bottomFrame = Frame()


label_a = Label(master=topFrame, text="hello world")
label_a.pack()



label_b = Label(master=bottomFrame, text="you2")
label_b.pack()

topFrame.pack()
bottomFrame.pack()



root.mainloop()