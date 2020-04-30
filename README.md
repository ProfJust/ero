# ERO
Aktueller Code zum Wahl-Modul (Bachelor) "Einführung in die Roboterprogrammierung mit ROS und Python", an der Westfälischen Hochschule - Campus Bocholt 

Anwendung:

     Klonen des Repositoriums 
     $ cd /catkin_ws/src/
     $ git clone https://github.com/ProfJust/ero
     
     Installieren der benötigten Pakete mit Shell-Skript
     $ cd /ero/ero_install
     $ chmod +x install_summit_pkg_on_remote_pc.sh
     $ ./install_summit_pkg_on_remote_pc.sh

     Kompilieren
     $ cd ~/catkin_ws/
     $ catkin_make
     
     alle Python-Skripte ausführbar setzen 
     $ cd ~/catkin_ws/src/ero/bin
     $ chmod --recursive +x .
     

jetzt kann man das gewünschte Python-Skript starten, z.B. 

     $ rosrun ero hello_world.py
     

jetzt kann man das gewünschte Launch-File starten, z.B. 
     
     $ roslaunch summit_xl_sim_bringup summit_xl_complete.launch move_base_robot_a:=true amcl_and_mapserver_a:=true localization_robot_a:=true id_robot_a:=summit_xl

Achtung: Im Ordner changed_summit_files sind die Änderungen zu den originalen Repositorien von Robotnik etc. zu finden. Bei Funktionsproblemen am besten erst mal hier reinschauen.
