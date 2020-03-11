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


jetzt kann man das gewünschte Launch-File starten, z.B. 

     $ roslaunch summit_xl_sim_bringup summit_xl_complete.launch move_base_robot_a:=true amcl_and_mapserver_a:=true localization_robot_a:=true id_robot_a:=summit_xl

