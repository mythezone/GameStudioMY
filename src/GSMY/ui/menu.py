# -*- encoding: utf-8 -*-
'''
@File    :   Menu.py
@Time    :   2022/01/07 23:16:27
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   Menu
'''

import tkinter as tk 

class Menu(object):
    def __init__(self,root=None,funcs={}) -> None:
        super().__init__()
        if root==None:
            self.root=tk.Tk()
        else:
            self.root=root
        self.menubar=tk.Menu(self.root)
        
        if funcs=={}:
            pass
        else:
            for k,v in funcs.items():
                self.menubar.add_command(label=k,command=v)
        
    def show(self):
        self.root.config(menu=self.menubar)
        
def nil():
    return None

class mainMenu(Menu):
    def __init__(self, root=None,funcs={}) -> None:
        super().__init__(root=root, funcs=funcs)
        
        # file菜单
        self.filemenu=tk.Menu(self.menubar,tearoff=False)
        self.menubar.add_cascade(label="文件",menu=self.filemenu)
        self.filemenu.add_command(label="新建项目",command=nil)
        self.filemenu.add_command(label="打开项目",command=nil)
        self.filemenu.add_command(label="关闭项目",command=nil)
        
        # edit菜单
        self.editmenu=tk.Menu(self.menubar,tearoff=False)
        self.menubar.add_cascade(label="文件",menu=self.editmenu)
        self.editmenu.add_command(label="撤销",command=nil)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="剪切",command=nil)
        self.editmenu.add_command(label="复制",command=nil)
        self.editmenu.add_command(label="粘贴",command=nil)
        self.editmenu.add_command(label="删除",command=nil)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="查找",command=nil)
        
        