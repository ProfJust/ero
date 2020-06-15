
# file_read_write_demo.py
# ---------------------------
# Vgl. Willemer Kap 14
# Hier aber Python V2
# 15.06.2020
# --------------------------

# --- Datei schreiben ---
# "w" => write
datei = open("poesiealbum.txt", "w")
datei.write("Zoegest Du die Beine ein\n")
datei.write("koenntest Du ne Kugel sein\n")
datei.close();

# "a" => append/ anhaengen
datei = open("poesiealbum.txt", "a")  
datei.write("Faehrst Du sie wieder aus\n")
datei.write("Siehts auch nicht anders aus\n")
datei.close()


# --- Daeit lesen ---
datei = open("poesiealbum.txt", "r")

# Liste aus Zeilen
zeilen = datei.readlines() 

datei.close()
for zeile in zeilen:
    print(zeile)