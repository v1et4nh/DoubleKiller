import cv2.cv2 as cv2  # pycharm specific
import os
import tkinter as tk

from tkinter import messagebox, filedialog, ttk


class App(tk.Tk):
    def __init__(self):
        # Set up Main Window
        tk.Tk.__init__(self)
        # Initialize parameters
        ROW = 0

        self.title = 'DoubleKiller'
        self.folder = ''

        # 1.Step: Select folder
        ROW += 1
        self.text1 = tk.Label(self, text='1. Select folder')
        self.text1.grid(row=ROW, column=0)
        ROW += 1
        # self.EntrySelectFolder = tk.Entry(self, width=44)
        # self.EntrySelectFolder.grid(row=ROW, column=0)
        self.BtnSelectFolder = tk.Button(self, text='Open Folder', command=self.openFolder)
        self.BtnSelectFolder.grid(row=ROW, column=0)

        # 2.Step: Select depth
        ROW += 1
        depthList = ("Same level", "Include all subfolder")
        variable = tk.StringVar(self)
        variable.set(depthList[0])
        self.combDepth = ttk.Combobox(self, textvariable=variable, state='readonly')
        self.combDepth['value'] = depthList
        self.combDepth.grid(row=ROW, column=0)
        self.combDepth.current(0)


    def openFolder(self):
        self.folder = filedialog.askdirectory(title='Select Folder')


def openFile(file):
    img = cv2.imread(file)
    return img


def showImg(img):
    cv2.imshow('', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    app = App()
    app.mainloop()
