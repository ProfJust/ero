# ERO
Aktueller Code zum Wahl-Modul (Bachelor) "Einführung in die Roboterprogrammierung mit ROS und Python", an der Westfälischen Hochschule - Campus Bocholt 

Anwendung:

     Klonen des Repositoriums - Version SS21 für ROS-Noetic
     $ cd /catkin_ws/src/
     $ git clone https://github.com/ProfJust/ero

     Ggf. ROS-Noetic installieren (Ubuntu 20.4, Focal Fossa)
     $ cd /ero/ero_install
     $ chmod +x ROS_Noetic_Installation_auf_Remote_PC.sh
     $ ./ROS_Noetic_Installation_auf_Remote_PC.sh
     
     Installieren der benötigten Pakete mit Shell-Skript
     $ cd /ero/ero_install
     $ chmod +x install_summit_pkg_on_noetic_remote_pc.sh
     $ ./install_summit_pkg_on_rnoetic_remote_pc.sh

     Kompilieren, geht nur im richtigen Verzeichnis
     $ cd ~/catkin_ws/
     $ catkin_make
     
     alle Python-Skripte ausführbar setzen 
     $ cd ~/catkin_ws/src/ero/bin
     $ chmod --recursive +x .
     

jetzt kann man das gewünschte Python-Skript starten, z.B. 

     $ rosrun ero hello_world.py
     

jetzt kann man das gewünschte Launch-File starten, z.B. 
den Summit_XL in der Willow-Garage

     $ roslaunch summit_xl_sim_bringup summit_xl_complete.launch move_base_robot_a:=true amcl_and_mapserver_a:=true
     
oder auf dem W-HS-Campus-Bocholt (dazu müssen die Map-Files an die richtigen Orte kopiert werden, siehe readMe dort)

     $ roslaunch summit_xl_sim_bringup summit_xl_complete.launch move_base_robot_a:=true amcl_and_mapserver_a:=true gazebo_world:=whs_world/whs.world map_file_a:=whs_world_map/whs.yaml

     stattdessen kann man auch unser eigenes Launch-File nehmen, dort wird sogar RViZ mitgestartet.

     $ roslaunch ero whs_summit_xl_complete.launch

     

bzw. in der leeren Welt 

     $ roslaunch ero summit_xl_in_empty_world.launch 

Achtung: Im Ordner changed_summit_files sind die Änderungen zu den originalen Repositorien von Robotnik etc. zu finden. Bei Funktionsproblemen am besten erst mal hier reinschauen.
