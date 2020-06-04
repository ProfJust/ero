whs_world_ReadMe.md
------------------------------------
Anleitung für die Gazebo- WHS-Welt, Campus Bocholt 


1.) Ordner  whs_world_rviz  kopieren nach  catkin_ws/src/summit_xl_common/maps  

2.) Ordner whs_world mit dem World File (und dae -meshes ) kopieren nach => ~/catkin_ws/src/summit_xl_sim/summit_xl_gazebo/worlds

3.) $ roslaunch ero whs_summit_xl_complete.launch 


4.) RViz: Fixed Frame auf robot_base_link konfigurieren

5.) Für Gazebo die Files ( meshes/whs_world_3D_Modell.dae, model.config, model.sdf)   nach ~/.gazebo/models/whs_world kopieren
