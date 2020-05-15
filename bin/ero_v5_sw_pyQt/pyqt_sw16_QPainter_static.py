#!/usr/bin/python
# -*- coding: utf-8 -*-
##pyqt_sw16_QPainter_static.py

# https://www.tutorialspoint.com/pyqt/pyqt_qpixmap_class.htm

import sys
from PyQt5.QtCore import (Qt)
from PyQt5.QtWidgets import (QWidget, QApplication)
from PyQt5.QtGui import QPainter, QColor, QFont


class Ui(QWidget):
    # statische Klassenvariablen
    pos_label_x = 20
    
    def __init__(self):  # Konstrukor
        # Konstruktor der Elternklasse aufrufen
        super(Ui, self).__init__()  
        self.initUI()
    
    def initUI(self):         
        self.text = " Ein ziemlich langer Text "
            
        # UI-Fenster Konfigurieren
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Qt - Painter')
        self.show()
        
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawFunc(event, painter)  # Funktion zum Zeichnen verbinden
        painter.end()
        
    def drawFunc(self, event, p):
        # Text zeichnen 
        p.setPen(QColor(168, 34, 3))
        p.setFont(QFont('Decorative', 10))
        p.drawText(event.rect(), Qt.AlignCenter, self.text)   
        
        # Linie zeichnen
        p.setPen(QColor(0, 200, 255))  # RGB 
        p.drawLine(10, 10, 450, 300)

        # Rechteck zeichnen
        p.setBrush(Qt.black)
        p.drawRect(10, 100, 30, 30)  # x,y,w,h
        
        p.setBrush(QColor(255, 0, 0))
        p.drawEllipse(200, 20, 25, 25)
                  
    
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec_())
