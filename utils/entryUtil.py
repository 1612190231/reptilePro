from tkinter import *
from tkinter import messagebox


def get_input(title, message):
    def return_callback(event):
        print('quit...')
        root.quit()

    def close_callback():
        root.destroy()
        # messagebox.askokcancel('message', 'no click...')

    root = Tk(className=title)
    root.wm_attributes('-topmost', 1)
    screenwidth, screenheight = root.maxsize()
    width = 600
    height = 100
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)
    root.resizable(0, 0)
    lable = Label(root, height=3)
    lable['text'] = message
    lable.pack()
    entry = Entry(root)
    entry.bind('<Return>', return_callback)
    entry.pack()
    entry.focus_set()
    root.protocol("WM_DELETE_WINDOW", close_callback)
    root.mainloop()
    url = entry.get()

    root.destroy()
    return url

