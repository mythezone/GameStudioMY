# -*- encoding: utf-8 -*-
'''
@File    :   toolbar.py
@Time    :   2022/01/07 23:51:04
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   filebar
'''

import tkinter as tk 

class Toolbar(object):
    def __init__(self,root=None) -> None:
        super().__init__()
        if root==None:
            self.root=tk.Tk()
        else:
            self.root=root
            
        self.toolbar=tk.Frame(self.root,relief=tk.RAISED,borderwidth=1)
        
        exitBtn=tk.Button(self.toolbar,text="退出",command=self.root.destroy)
        exitBtn.pack(side=tk.LEFT,padx=3,pady=3)
        self.toolbar.pack(side=tk.TOP,fill=tk.X)
    