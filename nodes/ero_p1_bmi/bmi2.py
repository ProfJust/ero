#!/usr/bin/env python
# bmi2.py
# ---------------------------------------
# 22.4.2012 by OJ - bis Zeile 23 gelynted
# 15.04.2021 by OJ => Python 3
# ---------------------------------------


def bmi(kg, m):
    bmi = kg/(m*m)
    return bmi


def bewertung(b, a):
    # Die Tabelle in einer konstanten Liste gespeichert (Tupel)
    matrix = ((19, 25, 35, 45, 55, 65, 1000),  # Alter Untergrenze Intervall
              (19, 20, 21, 22, 23, 24, 24),  # Untergrenze BMI
              (24, 25, 26, 27, 28, 29, 29))  # Obergrenze BMI
    i = 0
    while a >= matrix[0][i] and i < 6:
        i += 1

    if i >= 1:
        i = i-1  # einen zuerueck

    # debug Ausgabe
    print("Alter ", a, "Index i ", i, "OG ", matrix[2][i], "UG ", matrix[1][i])

    if(b > matrix[2][i]):
        print(" =>Uebergewicht")
    elif (b < matrix[1][i]):
        print(" => Untergewicht")
    else:
        print(" => Normalgewicht")


def main():
    gewicht = float(input("Geben Sie Ihr Gewicht in kg an \n"))
    laenge = float(input("Geben Sie Ihre Koerpergroesse in m an \n"))
    alter = float(input("Geben Sie Ihr Alter in Jahren an \n"))

    # input() gibt in Python3 einen String zurück => typecast nötig
    _bmi = bmi(gewicht, laenge)
    print("BMI: ", _bmi)
    bewertung(_bmi, alter)


# ------------------------------------------------------
main()
