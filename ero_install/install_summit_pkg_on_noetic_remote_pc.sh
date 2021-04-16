#!/bin/bash
# script to setup Summit_XL-Workspace

echo -e "\033[34m ---------- ERO SS21 - Workspace einrichten  ------------ \033[0m "

echo "Shellskript zur Installation der SummitXL-Pakete" 

sudo apt-get dist-upgrade
pwd
cd ~/catkin_ws/src/

mkdir -p ero_src

git clone https://github.com/RobotnikAutomation/summit_xl_sim
git clone https://github.com/RobotnikAutomation/summit_xl_common
git clone https://github.com/RobotnikAutomation/robotnik_msgs
git clone https://github.com/RobotnikAutomation/robotnik_sensors
git clone https://github.com/rst-tu-dortmund/costmap_prohibition_layer.git
git clone https://github.com/ros-planning/navigation.git
git clone https://github.com/cra-ros-pkg/robot_localization.git
git clone https://github.com/ros-geographic-info/geographic_info.git
git clone https://github.com/ros-geographic-info/unique_identifier.git

sudo apt-get dist-upgrade -y   #-y ist ohne Ja Abfrage
sudo apt-get update -y
sudo apt-get install ros-noetic-navigation -y
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


sudo apt-get install libsdl-image1.2-dev and
sudo apt-get install libsdl-dev

echo -e "\033[31m Aktualisiere alle Abhaengigkeiten der ROS-Pakete \033[0m"
rosdep update
rosdep install --from-paths src --ignore-src -r -y

echo -e "\033[31m to do:   $ cd ~/catkin_ws/  ...   catkin_make \033[0m"
