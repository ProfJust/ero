#!/bin/bash
# script to setup Summit_XL-Workspace
# Version vom 27.4.2021 incl Map directory kopieren

echo -e "\033[34m ---------- ERO SS21 - Workspace einrichten  ------------ \033[0m "

echo "Shellskript zur Installation der SummitXL-Pakete" 

sudo apt-get dist-upgrade
pwd
cd ~/catkin_ws/src/

# no noetic version available 15.4.21, so use melodic-devel
# siehe auch https://index.ros.org/p/summit_xl_gazebo/  etc.
git clone https://github.com/RobotnikAutomation/summit_xl_sim -b melodic-devel
git clone https://github.com/RobotnikAutomation/summit_xl_common -b melodic-devel
git clone https://github.com/RobotnikAutomation/robotnik_msgs -b melodic-devel
git clone https://github.com/RobotnikAutomation/robotnik_sensors -b melodic-devel
git clone https://github.com/rst-tu-dortmund/costmap_prohibition_layer.git

# noetic version available 15.4.21, so use it
git clone https://github.com/ros-planning/navigation.git -b noetic-devel
git clone https://github.com/cra-ros-pkg/robot_localization.git -b noetic-devel

git clone https://github.com/ros-geographic-info/geographic_info.git 
git clone https://github.com/ros-geographic-info/unique_identifier.git
git clone https://github.com/ccny-ros-pkg/imu_tools.git -b noetic

sudo apt-get dist-upgrade -y   #-y ist ohne Ja Abfrage
sudo apt-get update -y
# Test
sudo apt-get install ros-$(rosversion -d)-navigation -y
sudo apt-get install ros-noetic-robot-localization -y
sudo apt-get install ros-noetic-mavros-* -y
sudo apt-get install ros-noetic-gmapping -y
sudo apt-get install ros-noetic-teb-local-planner -y
sudo apt-get install ros-noetic-costmap-prohibition-layer -y
sudo apt-get install ros-noetic-summit-xl-robot-control -y
sudo apt-get install ros-noetic-nmea-navsat-driver -y
sudo apt-get install ros-noetic-twist-mux -y
sudo apt-get install ros-noetic-gazebo-ros-control -y
sudo apt-get install ros-noetic-twist-mux -y
sudo apt-get install ros-noetic-teleop-twist-keyboard -y
sudo apt-get install ros-noetic-tf2-sensor-msgs -y
sudo apt-get install ros-noetic-velocity-controllers -Y
# added by OJ 16.04.21
sudo apt-get install ros-noetic-velocity-controllers -y
# added by OJ 28.4.21
sudo apt-get install pyqt5-dev-tools -y


sudo apt-get install libsdl-image1.2-dev and
sudo apt-get install libsdl-dev

echo -e "\033[31m Aktualisiere alle Abhaengigkeiten der ROS-Pakete \033[0m"
rosdep update
rosdep install --from-paths src --ignore-src -r -y

echo -e "\033[34m copying WHS-Map directories to Robotnik-Packages \033[0m"
cp -a ~/catkin_ws/src/ero/ero_gz_worlds/whs_world_map/.  ~/catkin_ws/src/summit_xl_common/summit_xl_localization/maps/whs_world_map
cp -a ~/catkin_ws/src/ero/ero_gz_worlds/whs_world_model/.  ~/.gazebo/models/whs_world_model
cp -a ~/catkin_ws/src/ero/ero_gz_worlds/whs_world/.  ~/catkin_ws/src/summit_xl_sim/summit_xl_gazebo/worlds

echo -e "\033[31m to do:   $ cd ~/catkin_ws/  ...   catkin_make \033[0m"
