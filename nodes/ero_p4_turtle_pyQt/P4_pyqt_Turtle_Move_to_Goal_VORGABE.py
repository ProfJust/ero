#!/usr/bin/env python3
# --- P4_pyqt_Turtle_Move_to Goal_VORGABE.py ------
# Version vom 29.4.2021 by OJ
# Vorgabe für das P4,
# PyQt-GUI für die Steuerung der TurtleSim
# ----------------------------------
# Starten von ROS und der TurtleSim
# $1 roscore
# $2 rosrun turtlesim turtlesim_node
# $3 rosrun ero P4_pyqt_Turtle_Move_to_Goal_VORGABE.py
# (vorher catkin_make und ausführbar machen mit chmod +x)
# PyQt muss installiert sein
# sudo apt-get install pyqt5-dev-tools
# ------------------------------------------

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QPushButton, QVBoxLayout, QHBoxLayout,
                             QApplication, QLabel)

# --- Import (Include) der Klassendefinition ----
# Dieses File muss im selben Ordner liegen
import TurtleSimClassDef


class TurtleUIClass(QWidget):
    def __init__(self):  # Konstrukor
        # Konstruktor der Elternklasse aufrufen
        super(TurtleUIClass, self).__init__()
        self.initUI()

    def initUI(self):
        # Instanziierung der Widgets
        startWert = 5
        self.lcd = QLCDNumber(self)
        self.lcd.display(startWert)
        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.setMaximum(11)
        self.sld.setMinimum(0)
        self.sld.setValue(startWert)
        self.pbLess = QPushButton('<')
        self.pbMore = QPushButton('>')
        self.pbGo = QPushButton(' Go Turtle ')
        self.lblStatus = QLabel('Statuszeile')

        # BOX-Layout mit Widgets füllen
        vbox = QVBoxLayout()
        # 1.Reihe
        vbox.addWidget(self.lcd)
        # 2.Reihe
        vbox.addWidget(self.sld)
        # 3.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(self.pbLess)
        hbox.addWidget(self.pbMore)

        vbox.addLayout(hbox)
        # 4.Reihe
        vbox.addWidget(self.pbGo)
        # Alle Boxen ins Window setzen
        self.setLayout(vbox)

        # Signal und Slot verbinden
        self.sld.valueChanged.connect(self.lcd.display)
        self.sld.valueChanged.connect(self.lcd.display)

        self.pbLess.clicked.connect(self.SlotKlick)
        self.pbMore.clicked.connect(self.SlotKlick)
        self.pbGo.clicked.connect(self.SlotGo)

        # Fenster Konfigurieren
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('ERO - PyQt - TurtleSteering')
        self.show()

    def SlotKlick(self):
        sender = self.sender()
        self.lblStatus.setText(sender.text() + ' was pressed')
        if sender.text() == '<':
            wert = self.sld.value()
            wert = wert-1
            self.sld.setValue(wert)
        else:
            wert = self.sld.value()
            wert = wert+1
            self.sld.setValue(wert)

    def SlotGo(self):
        """ Hier geht die Turtle ab """
        turtle1.goal.x = self.sld.value()
        turtle1.goal.y = self.sld.value()
        turtle1.move2goal()


if __name__ == '__main__':
    # to avoid NameError: name 'TurtleClass' is not defined
    # use the filename followed by  "." here
    turtle1 = TurtleSimClassDef.TurtleSimClass("turtle1")

    app = QApplication(sys.argv)
    ex = TurtleUIClass()
    sys.exit(app.exec_())
