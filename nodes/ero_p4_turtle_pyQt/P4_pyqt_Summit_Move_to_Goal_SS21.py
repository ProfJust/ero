#!/usr/bin/env python3
# --- P4_pyqt_Summit_Move_to Goal_SS21.py ------
# Version vom 6.5.2021 by OJ
# PyQt-GUI für die Steuerung des Summit
# --------------------------------------------------
# Starten von ROS und Gazebo
#
# $1 roslaunch ero summit_xl_in_empty_world.launch
# $3 rosrun P4_pyqt_Summit_Move_to_Goal_SS21.py
#
# PyQt muss installiert sein
# sudo apt-get install pyqt5-dev-tools
#
# Hier gibt es kein Pose-Topic, nur die Odometrie
# des Summit /robot/robotnik_base_control/odom
# Problem: Sobald der Summit dreht, stimmt die Odometrie
# - Pose nicht mehr mit der Gazebo-Welt überein
# --------------------------------------------------

import sys
from math import pi
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QPushButton, QVBoxLayout, QHBoxLayout,
                             QApplication, QLabel)

# --- Import (Include) der Klassendefinition ----
# Dieses File muss im selben Ordner liegen
import SummitClassDef


class SummitUIClass(QWidget):
    def __init__(self):  # Konstrukor
        # Konstruktor der Elternklasse aufrufen
        super(SummitUIClass, self).__init__()
        self.initUI()

    def initUI(self):
        # Instanziierung der Widgets
        startWertX = 3
        self.lcdX = QLCDNumber(self)
        self.lcdX.display(startWertX)

        startWertY = 0
        self.lcdY = QLCDNumber(self)
        self.lcdY.display(startWertY)

        # startWertT = 0  # Theta in Grad
        # self.lcdT = QLCDNumber(self)
        # self.lcdT.setDecMode()
        # self.lcdT.display(startWertT)

        self.sldX = QSlider(Qt.Horizontal, self)
        self.sldX.setMaximum(10)
        self.sldX.setMinimum(-10)
        self.sldX.setValue(startWertX)

        self.sldY = QSlider(Qt.Horizontal, self)
        self.sldY.setMaximum(10)
        self.sldY.setMinimum(-10)
        self.sldY.setValue(startWertY)

        # self.sldT = QSlider(Qt.Horizontal, self)
        # self.sldT.setMaximum(180)
        # self.sldT.setMinimum(-180)
        # self.sldT.setValue(startWertY)

        self.pbLessX = QPushButton('<')
        self.pbMoreX = QPushButton('>')
        self.pbLessY = QPushButton('<')
        self.pbMoreY = QPushButton('>')
        # self.pbLessT = QPushButton('<')
        # self.pbMoreT = QPushButton('>')

        self.pbGo = QPushButton(' Go to Goal - Summit!')
        # self.lblGoal = QLabel("""Goal:                   X  [m]      \
        #                       Y [m]                        \
        #                       Theta [Grad]""")
        self.lblGoal = QLabel("""Goal:                   X  [m]      \
                              Y [m] """)

        # BOX-Layout mit Widgets füllen
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addWidget(self.lblGoal)
        # 1.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(self.lcdX)
        hbox.addWidget(self.lcdY)
        # hbox.addWidget(self.lcdT)
        vbox.addLayout(hbox)
        # 2.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(self.sldX)
        hbox.addWidget(self.sldY)
        # hbox.addWidget(self.sldT)
        vbox.addLayout(hbox)

        # 3.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(self.pbLessX)
        hbox.addWidget(self.pbMoreX)
        hbox.addWidget(self.pbLessY)
        hbox.addWidget(self.pbMoreY)
        # hbox.addWidget(self.pbLessT)
        # hbox.addWidget(self.pbMoreT)
        vbox.addLayout(hbox)

        # 4.Reihe
        vbox.addWidget(self.pbGo)
        # Alle Boxen ins Window setzen
        self.setLayout(vbox)

        # Signal und Slot verbinden
        self.sldX.valueChanged.connect(self.lcdX.display)
        self.sldY.valueChanged.connect(self.lcdY.display)
        # self.sldT.valueChanged.connect(self.lcdT.display)

        self.pbLessX.clicked.connect(self.SlotKlickX)
        self.pbMoreX.clicked.connect(self.SlotKlickX)
        self.pbLessY.clicked.connect(self.SlotKlickY)
        self.pbMoreY.clicked.connect(self.SlotKlickY)
        # self.pbLessT.clicked.connect(self.SlotKlickT)
        # self.pbMoreT.clicked.connect(self.SlotKlickT)
        self.pbGo.clicked.connect(self.SlotGo)

        # Fenster Konfigurieren
        self.setGeometry(300, 300, 200, 150)
        self.setWindowTitle('ERO - PyQt - SummitSteering')
        self.show()

    def SlotKlickX(self):
        sender = self.sender()
        if sender.text() == '<':
            wert = self.sldX.value()
            wert = wert-1
            self.sldX.setValue(wert)
        else:
            wert = self.sldX.value()
            wert = wert+1
            self.sldX.setValue(wert)

    def SlotKlickY(self):
        sender = self.sender()
        if sender.text() == '<':
            wert = self.sldY.value()
            wert = wert-1
            self.sldY.setValue(wert)
        else:
            wert = self.sldY.value()
            wert = wert+1
            self.sldY.setValue(wert)

    def SlotKlickT(self):
        sender = self.sender()
        if sender.text() == '<':
            wert = self.sldT.value()
            wert = wert - 10
            self.sldT.setValue(wert)
        else:
            wert = self.sldT.value()
            wert = wert + 10
            self.sldT.setValue(wert)

    def SlotGo(self):
        """ Hier geht die Turtle ab """
        mySummit.goal.x = self.sldX.value()
        mySummit.goal.y = self.sldY.value()
        # mySummit.goal.theta = self.sldT.value() / 180 * pi
        mySummit.move2goal()


if __name__ == '__main__':
    # to avoid NameError: name 'TurtleClass' is not defined
    # use the filename followed by  "." here
    mySummit = SummitClassDef.SummitClass("Summit")

    app = QApplication(sys.argv)
    ex = SummitUIClass()
    sys.exit(app.exec_())
