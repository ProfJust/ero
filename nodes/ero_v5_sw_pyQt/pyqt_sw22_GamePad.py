#!/usr/bin/python3
# -*- coding: utf-8 -*-
##pyqt_sw22_GamePad.py



# https://github.com/zeth/inputs
# sudo pip install inputs
# => DragonRise Inc.   Generic   USB  Joystick


import sys
from PyQt5.QtCore import (Qt, QTimer, QRect)
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel)
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtGui import QPixmap, QKeyEvent
from inputs import devices
from inputs import get_gamepad

global ballsize
ballsize = 40

global keepersize
keepersize = 50

class Ui(QWidget):
    #statische Klassenvariablen
    pos_x = 200
    pos_y = 20
    pos_keeper = 200
    speed_x = +5
    speed_y = -6
    keyLeft = False
    keyRight = False
    
    def __init__(self): #Konstrukor
        #Konstruktor der Elternklasse aufrufen
        super(Ui, self).__init__()  
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)  
        self.timer.start(20) 
        #Gamepad
        print("We have detected the following devices:\n")
        for device in devices:
            print(device)   
                
        self.initUI()
    
    def initUI(self):         
        #UI-Fenster Konfigurieren
        self.setGeometry(30, 30, 600, 600)
        self.setWindowTitle('Qt - Painter')
        self.show()
        
    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        self.drawFunc(event, p)        
        p.end()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.keyLeft = True
        if event.key() == Qt.Key_Right:
            self.keyRight = True
            
    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Left:
             self.keyLeft = False
        if event.key() == Qt.Key_Right:
             self.keyRight = False
        event.accept()
        
    def drawFunc(self, event, p):            
        #Hintergrund mit Pixmap        
        pix = QPixmap("gras.jpg") 
        p.drawPixmap(self.rect(),pix)
        
        # Ball: bewegtes Rechteck zeichnen mit Pixmap          
        pix2 = QPixmap("ball_transparent.png")  #PNG mit Transparenz
        target =  QRect(self.pos_x,self.pos_y,ballsize,ballsize) #import QRect
        p.drawPixmap(target,pix2)
            
        #Keeper
        p.setBrush(QColor(0, 0, 0))#RGB 
        p.drawRect(self.pos_keeper,570,keepersize*2,20)
        
    def update(self): 
        # Gamepad lesen
        events = get_gamepad()
        for event in events:
            #print(event.ev_type, event.code, event.state)
            if event.code == 'ABS_Z' and event.state >= 140:
                print('Right')
                self.pos_keeper  = self.pos_keeper  + 5
                break
            if event.code == 'ABS_Z' and event.state <= 130:
                print('Left')
                self.pos_keeper  = self.pos_keeper  - 5
                break
            
        
        self.pos_x = self.pos_x + self.speed_x
        self.pos_y = self.pos_y + self.speed_y
        if self.pos_x < 0:
            self.speed_x = -self.speed_x
        if self.pos_x > 600-ballsize:
            self.speed_x = -self.speed_x       
        if self.pos_y < 0:
            self.speed_y = -self.speed_y
        #Keeper
        if self.keyLeft==True  and self.pos_keeper >=10:
                self.pos_keeper  = self.pos_keeper  - 5
        if self.keyRight==True and self.pos_keeper <=500:
                self.pos_keeper  = self.pos_keeper  + 5
        #Ball am Keeper
        if self.pos_y > 540:
            if (self.pos_x <= (self.pos_keeper + keepersize+ballsize)) and (self.pos_x >= (self.pos_keeper - keepersize)):
                self.speed_y = -self.speed_y
                self.pos_y = self.pos_y + self.speed_y
                
            else:
                pass
                #print("Game Over " + str(self.pos_x)+" " +str(self.pos_keeper ))
                #sys.exit()
                    
        self.repaint()
##    def event_loop(events):
####        '''
####        This function is called in a loop, and will get the events from the
####        controller and send them to the functions we specify in the `event_lut`
####        dictionary
####        '''
##        for event in events:
##            print('\t', event.ev_type, event.code, event.state)
##            call = event_lut.get(event.code)
##            if callable(call):
##               call(event.state)
##    
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec_())