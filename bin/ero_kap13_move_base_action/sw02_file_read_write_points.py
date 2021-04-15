
# file_read_write_demo.py
# ---------------------------
# Vgl. Willemer Kap 14
# Hier aber Python V2
# 15.06.2020
# --------------------------

# --- Datei schreiben ---
# "w" => write
# "a" => append/ anhaengen
datei = open("points.txt", "w")
datei.write("[(-3.39, 1.95, 0.000), (0.000, 0.000, -0.990, 0.114)] \n")
datei.write("[(4.547, -2.71, 0.000), (0.000, 0.000, -0.775, 0.655)] \n")
datei.write("[(-3.757, -1.03, 0.000), (0.000, 0.000, 0.010, 0.999)] \n")
datei.close()

# --- Datei lesen ---
datei = open("points.txt", "r")

# Liste aus Zeilen
zeilen = datei.readlines() 

datei.close()
for zeile in zeilen:
    print(zeile)