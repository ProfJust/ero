#!/usr/bin/env python
# --------------------------------------------------------------
# class_kiste.py
# --------------------------------------------------------------
# vgl. Willemer http://www.willemer.de/informatik/python/klasse.htm
# --------------------------------------------------------------
# OJ, 30.4.2020
# ----------------------------------------------------------------


class Kiste:
    def __init__(self, name):  # Konstruktor
        self._breite = 0
        self._hoehe = 0
        self._tiefe = 0
        self._vol = -1
        self._name = name

    def setBreite(self, breite):  # Setter
        if self._breite != breite:
            self._breite = breite
            self._vol = -1

    def setHoehe(self, hoehe):  # Setter
        if self._hoehe != hoehe:
            self._hoehe = hoehe
            self._vol = -1

    def setTiefe(self, tiefe):  # Setter
        if self._tiefe != tiefe:
            self._tiefe = tiefe
            self._vol = -1

    def getVolumen(self):  # Getter
        if (self._vol == -1):
            print("calc", self._name)
            self._vol = self._breite*self._hoehe*self._tiefe
        return self._vol

    def getName(self):
        return self._name


if __name__ == '__main__':
    kiste = Kiste("Kiste Nr .1")  # Konstruktor
    kiste.setBreite(2)
    kiste.setHoehe(3)
    kiste.setTiefe(4)
    print(kiste.getName(), kiste.getVolumen())
    
    kiste2 = Kiste("Kiste Nr. 2") # Konstruktor
    kiste2.setHoehe(3)
    print(kiste2.getVolumen())
    kiste2.setBreite(1)
    kiste2.setTiefe(2)
    # illegaler Zugriff auf private Variable _name
    print(kiste2._name, kiste2.getVolumen()) 
