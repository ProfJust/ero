#!/usr/bin/env python
# BMI.py
# # -----------------------------------
# 17.09.2018 by OJ
# -----------------------------------


def bmi(m, l):
    bmi = m/(l*l)
    return bmi


def bewertung(b):
    if (b > 25):
		print(" => Uebergewicht")
	elif (b < 18.5):
		print(" => Untergewicht")
	else:	
		print(" => Normalgewicht")


def main():    
	gewicht = input("Geben Sie Ihr Gewicht in kg an \n")
	laenge  = input("Geben Sie Ihre Koerpergroesse in m an \n")
	#alter   = input("Geben Sie Ihr Alter in Jahren an \n");

	_bmi = bmi(gewicht, laenge)
	
	print("BMI: ",_bmi)
	bewertung(_bmi)
		

# ------------------------------------------------------
main()
