Standard launch:
$ roslaunch summit_xl_sim_bringup summit_xl_complete.launch move_base_robot_a:=true amcl_and_mapserver_a:=true localization_robot_a:=true

=> ersetzt durch 
$ roslaunch whs_summit_xl_complete.launch

dort ist 
 	move_base_robot_a:=true 
	amcl_and_mapserver_a:=true 
	localization_robot_a:=true



Map File (pgm und yaml) kopieren nach => catkin_ws/src/summit_xl_common/summit_xl_localization/maps/whs_world

Map erscheint in rviz => OK


Gazebo: WHS-Model erscheint nicht.
=> Lösung: neues Model anlegen in Gazebo unter Nutzung des dae-Files


