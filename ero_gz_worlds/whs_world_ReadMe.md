### whs_world_ReadMe.md
------------------------------------
**Jetzt funktioniert es! 4.6.20, 17:10 Uhr**
** => in Install-Skript eingefügt **
Anleitung zum Start der Summit-Simulation mit dem Campus Bocholt - Model whs_world.world
...
$ cp -a /source/. /dest/
$ cp -a ~/catkin_ws/src/ero/ero_gz_worlds/whs_world_map/.  ~/catkin_ws/src/summit_xl_common/summit_xl_localization/maps/whs_world_map
$ cp -a ~/catkin_ws/src/ero/ero_gz_worlds/whs_world_model/.  ~/.gazebo/models/whs_world_model
$ cp -a ~/catkin_ws/src/ero/ero_gz_worlds/whs_world/.  ~/catkin_ws/src/summit_xl_sim/summit_xl_gazebo/worlds

1. Ordner  __whs_world_map__  kopieren nach  __catkin_ws/src/summit_xl_common/summit_xl_localization/maps/..__ 

2. Ordner __whs_world_model__ kopieren nach __~/.gazebo/models/..__ kopieren (Achtung Verborgene Dateien)

3. File __whs_world.world__  kopieren nach __~/catkin_ws/src/summit_xl_sim/summit_xl_gazebo/worlds__

4. **$ roslaunch ero whs_summit_xl_complete.launch

5. RViz: Fixed Frame auf __robot_map__ konfigurieren




