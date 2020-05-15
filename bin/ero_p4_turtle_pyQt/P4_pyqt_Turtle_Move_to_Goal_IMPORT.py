#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QPushButton, QVBoxLayout, QHBoxLayout,
                             QApplication, QLabel)


import TurtleBotClass_File
		

class TurtleUIClass(QWidget):	

    def __init__(self): #Konstrukor
		#Konstruktor der Elternklasse aufrufen
		super(TurtleUIClass, self).__init__()   
		self.initUI()
				
    def initUI(self): 
		#Instanziierung der Widgets    
		startWert = 5  
		self.lcd = QLCDNumber(self)
		self.lcd.display(startWert)
		self.lcdY = QLCDNumber(self)
		self.lcdY.display(startWert)
		
		self.sld = QSlider(Qt.Horizontal, self)
		self.sld.setMaximum(11)
		self.sld.setMinimum(0)
		self.sld.setValue(startWert)
		self.sldY = QSlider(Qt.Horizontal, self)
		self.sldY.setMaximum(11)
		self.sldY.setMinimum(0)
		self.sldY.setValue(startWert)
		
		self.pbLess = QPushButton('<')
		self.pbMore = QPushButton('>')
		self.pbLessY = QPushButton('<')
		self.pbMoreY = QPushButton('>')
		
		self.pbGo = QPushButton(' Go Turtle ')
		self.lblStatus = QLabel('Statuszeile')
		
		#BOX-Layout mit Widgets füllen
		vbox = QVBoxLayout()
		#1.Reihe   
		hbox = QHBoxLayout()     
		hbox.addWidget(self.lcd)
		hbox.addWidget(self.lcdY)
		# =>
		vbox.addLayout(hbox)
		#2.Reihe
		hbox = QHBoxLayout()    
		hbox.addWidget(self.sld)
		hbox.addWidget(self.sldY)
		vbox.addLayout(hbox)
		#3.Reihe
		hbox = QHBoxLayout()
		hbox.addWidget(self.pbLess)
		hbox.addWidget(self.pbMore)
		hbox.addWidget(self.pbLessY)
		hbox.addWidget(self.pbMoreY)
		vbox.addLayout(hbox)
		#4.Reihe
		vbox.addWidget(self.pbGo)
		#Alle Boxen ins Window setzen        
		self.setLayout(vbox)           
		
		# Signal und Slot verbinden
		self.sld.valueChanged.connect(self.lcd.display)
		self.sld.valueChanged.connect(self.lcd.display)
		self.sldY.valueChanged.connect(self.lcdY.display)
		self.sldY.valueChanged.connect(self.lcdY.display)
		""" Hier geht die Turtle ab """
		
		self.pbLess.clicked.connect(self.SlotKlick)
		self.pbMore.clicked.connect(self.SlotKlick)
		self.pbLessY.clicked.connect(self.SlotKlickY)
		self.pbMoreY.clicked.connect(self.SlotKlickY)
		
		self.pbGo.clicked.connect(self.SlotGo)
		
		#Fenster Konfigurieren
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('ROP - PyQt - TurtleSteering')
		self.show()
		
    def SlotKlick(self):
		sender = self.sender()
		self.lblStatus.setText(sender.text() + ' was pressed')   
		if sender.text()=='<':
			wert = self.sld.value()
			wert = wert-1
			self.sld.setValue(wert)  
		else:
			wert = self.sld.value()
			wert = wert+1
			self.sld.setValue(wert)
			
    def SlotKlickY(self):
		sender = self.sender()
		if sender.text()=='<':
			wert = self.sldY.value()
			wert = wert-1
			self.sldY.setValue(wert)  
		else:
			wert = self.sldY.value()
			wert = wert+1
			self.sldY.setValue(wert)
			
    def SlotGo(self):
		""" Hier geht die Turtle ab """
		turtle1.goal.x = self.sld.value()
		turtle1.goal.y = self.sldY.value()
		turtle1.move2goal()
		
if __name__ == '__main__':    
	turtle1 = TurtleBotClass_File.TurtleBotClass()
	
	app = QApplication(sys.argv)
	ex = TurtleUIClass()
	sys.exit(app.exec_())
