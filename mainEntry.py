from tkinter import *
from tkinter.messagebox import showinfo


def jd():
    showinfo(title='新窗口', message='另一个窗口')


if __name__ == "__main__":
    root = Tk(className="首页")
    root.wm_attributes('-topmost', 1)
    screenwidth, screenheight = root.maxsize()
    width = 300
    height = 240
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)
    root.resizable(0, 0)

    lable1 = Label(root, height=2)
    lable1['text'] = "京东comment"
    lable1.place(x=50, y=20)
    button1 = Button(root, text='press', command=jd)
    button1.place(x=200, y=20)

    lable2 = Label(root, height=2)
    lable2['text'] = "淘宝comment"
    lable2.place(x=50, y=60)
    button2 = Button(root, text='press', command=jd)
    button2.place(x=200, y=60)

    lable3 = Label(root, height=2)
    lable3['text'] = "小红书截图"
    lable3.place(x=50, y=100)
    button3 = Button(root, text='press', command=jd)
    button3.place(x=200, y=100)

    lable4 = Label(root, height=2)
    lable4['text'] = "小红书clipping"
    lable4.place(x=50, y=140)
    button4 = Button(root, text='press', command=jd)
    button4.place(x=200, y=140)

    lable5 = Label(root, height=2)
    lable5['text'] = "小红书app评论"
    lable5.place(x=50, y=180)
    button5 = Button(root, text='press', command=jd)
    button5.place(x=200, y=180)

    root.mainloop()
