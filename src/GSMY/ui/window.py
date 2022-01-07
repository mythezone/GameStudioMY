# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2022/01/07 22:49:22
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   Window
'''

import tkinter as tk 
from tkinter import messagebox
from menu import *
from toolbar import *
from statusbar import *

class Window(object):
    
    def __init__(self,root=None,title="Default",geomitry=(1080,720),resizable=(True,True),maxsize=(1920,1080),minsize=(720,480),configure={},iconbitmap="") -> None:
        """[summary]

        Args:
            root ([type], optional): [description]. Defaults to None.
            title (str, optional): [description]. Defaults to "Default".
            geomitry (str, optional): [description]. Defaults to "1080x720+500+500".
            resizable (tuple, optional): [description]. Defaults to (True,True).
            maxsize (tuple, optional): [description]. Defaults to (1920,1080).
            minsize (tuple, optional): [description]. Defaults to (720,480).
            configure (dict, optional): [description]. Defaults to {}.
            iconbitmap (str, optional): [description]. Defaults to "".
        """
        super().__init__()
        
        if root == None:
            self.root = tk.Tk()
        else:
            self.root = root
            
        self.screenwidth=self.root.winfo_screenwidth()
        self.screenheight=self.root.winfo_screenheight()
        
        self.root.title(title)
        
        # 窗口居中显示
        tmp_geo="%dx%d+%d+%d"%(geomitry[0],geomitry[1],(self.screenwidth-geomitry[0])//2,(self.screenheight-geomitry[1])//2)
        self.root.geometry(tmp_geo)
        
        # 窗口大小调整
        self.root.resizable(*resizable)
        self.root.maxsize(*maxsize)
        self.root.minsize(*minsize)
        
        # 窗口的icon设置
        if iconbitmap!="":
            self.root.iconbitmap(iconbitmap)
            
        # 添加各种组件
        
        
    def add_menu(self,funcs):
        m=Menu(root=self.root,funcs=funcs)
        m.show()
        
    def show(self):
        self.root.mainloop()
        
        
class mainWindow(Window):
    def __init__(self, root=None, title="主窗口 - GameStudio MY", geomitry=(1080, 720), resizable=(True, True), maxsize=(1920, 1080), minsize=(720, 480), configure={}, iconbitmap="") -> None:
        super().__init__(root=root, title=title, geomitry=geomitry, resizable=resizable, maxsize=maxsize, minsize=minsize, configure=configure, iconbitmap=iconbitmap)
        self.add_mainmenu()
        self.add_toolbar()
        self.add_statusbar()
        
    def add_mainmenu(self):
        m=mainMenu(root=self.root)
        m.show()
        
    def add_toolbar(self):
        t=Toolbar(root=self.root)
        
    def add_statusbar(self):
        s=StatusBar(root=self.root)
        
def hello():
    messagebox.showinfo("Hello","欢迎使用菜单！")
    

if __name__ == '__main__':
    funcs={"Hello!":hello}
    w=mainWindow()
    w.show()