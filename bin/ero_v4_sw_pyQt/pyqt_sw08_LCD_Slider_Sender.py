#!/usr/bin/python
# -*- coding: utf-8 -*-

# sigslot.py
"""
ZetCode PyQt5 tutorial

In this example, we connect a signal
of a QSlider to a slot of a QLCDNumber.

Author: Jan Bodnar
Website: zetcode.com
Last edited: January 2017
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QPushButton, QVBoxLayout, QHBoxLayout,
                             QApplication, QLabel)


class Example(QWidget):

    def __init__(self):  # Konstrukor
        # OJ super().__init__()
        # Konstruktor der Elternklasse aufrufen
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # Instanziierung der Widgets
        lcd = QLCDNumber(self)
        self.sld = QSlider(Qt.Horizontal, self)
        pbLess = QPushButton('<')
        pbMore = QPushButton('>')
        self.lblStatus = QLabel('Statuszeile')

        # BOX-Layout mit Widgets füllen
        vbox = QVBoxLayout()
        # 1.Reihe
        vbox.addWidget(lcd)
        # 2.Reihe
        vbox.addWidget(self.sld)
        # 3.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(pbLess)
        hbox.addWidget(pbMore)
        vbox.addLayout(hbox)
        # 4.Reihe
        vbox.addWidget(self.lblStatus)
        # Alle Boxen ins Window setzen
        self.setLayout(vbox)
        # Signal und Slot verbinden
        self.sld.valueChanged.connect(lcd.display)
        self.sld.valueChanged.connect(lcd.display)
        pbLess.clicked.connect(self.SlotKlick)
        pbMore.clicked.connect(self.SlotKlick)
        # Fenster Konfigurieren
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
