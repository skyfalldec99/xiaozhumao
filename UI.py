import sys
import easygui as g
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5 import QtGui
import os 
from typein import typeinformation
from material import getmaterial
from mesh import gettxt
from calculate import  calcu
import numpy as np
from show import showpic
from PyQt5.QtGui import QFont
class Example(QMainWindow):
    def __init__(self):
        super().__init__()        
        self.initUI()
    def initUI(self):
        font = QtGui.QFont()

        font.setFamily('宋体')

        font.setBold(True)

        font.setPointSize(13)
        font.setWeight(75)

        btn1 = QPushButton("GMSH建模", self) 
        btn1.move(350, 100)
        btn1.resize(200,100)
        btn1.setFont(font)


        btn2 = QPushButton("荷载，约束和材料信息输入", self)
        btn2.move(220, 300)
        btn2.resize(500,100)
        btn2.setFont(font)


        btn3 = QPushButton("计算", self)
        btn3.move(390, 500)
        btn3.resize(100,60)
        btn3.setFont(font)


        btn4 = QPushButton("绘图", self)
        btn4.move(390, 700)
        btn4.resize(100,60)
        btn4.setFont(font)



        btn1.clicked.connect(self.buttonClicked1)            
        btn2.clicked.connect(self.buttonClicked2)
        btn3.clicked.connect(self.buttonClicked3)            
        btn4.clicked.connect(self.buttonClicked4)

        self.statusBar()        
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('hjx有限元程序')
        self.show()       


    def buttonClicked1(self):     
        sender = self.sender()
        self.setStyleSheet("color:purple;")
        self.statusBar().showMessage(sender.text() + ' was pressed')
        title = g.msgbox(msg="打开你的gmsh.exe",title="hjx有限元程序",ok_button="试一试")
        file_path1=g.fileopenbox(default="*.exe")
        #当然你也可以指定信息参数和标题参数
        main =file_path1
        os.popen(main)   
    def buttonClicked2(self): 
        global E,nu,m,n,ty      
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ty=typeinformation()
        [E,nu]=getmaterial()
        [m,n]=gettxt()
    def buttonClicked3(self):  
        global ns,es,x,y,s     
        sender=self.sender()
        print(E)
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ns=np.loadtxt(n) 
        es=np.loadtxt(m)
        x=ns[:,1]
        y=ns[:,2] 
        #建节点和单元
        s=calcu(ns,es,x,y,E,nu,ty)
    def buttonClicked4(self):          
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        #获取节点坐标
        showpic(s)
               
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())