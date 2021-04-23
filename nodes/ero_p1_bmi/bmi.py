#!/usr/bin/env python
# BMI.py
# # -----------------------------------
# 15.04.2021 by OJ => Python 3
# -----------------------------------


def bmi(kg, m):
    bmi = kg/(m*m)
    return bmi


def bewertung(b):
    if (b > 25):
        print(" => Uebergewicht")
    elif (b < 18.5):
        print(" => Untergewicht")
    else:
        print(" => Normalgewicht")


def main():
    # input() gibt in Python3 einen String zurück => typecast nötig
    gewicht = float(input("Geben Sie Ihr Gewicht in kg an \n"))
    laenge = float(input("Geben Sie Ihre Koerpergroesse in m an \n"))

    _bmi = bmi(gewicht, laenge)

    print("BMI: ", _bmi)
    bewertung(_bmi)


# ------------------------------------------------------
main()
