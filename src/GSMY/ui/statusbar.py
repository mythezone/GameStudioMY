# -*- encoding: utf-8 -*-
'''
@File    :   statusbar.py
@Time    :   2022/01/08 00:07:39
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   statusbar
'''

import tkinter as tk 

class StatusBar(object):
    def __init__(self,root=None) -> None:
        super().__init__()
        if root==None:
            self.root=tk.Tk()
        else:
            self.root=root
        self.statusbar=tk.Label(self.root,text="     |       | 100%  | 自动 ",bd=1,relief=tk.SUNKEN,anchor=tk.W)
        self.statusbar.pack(side=tk.BOTTOM,fill=tk.X)