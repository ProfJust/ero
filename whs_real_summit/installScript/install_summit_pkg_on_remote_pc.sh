#!/bin/bash
# script to setup Summit_XL-Workspace with ROS Melodic
# based on https://github.com/ProfJust/ero/blob/master/ero_install/install_summit_pkg_on_remote_pc.sh

echo -e "\033[1;92m ---------- Skript zur Einrichtung des SummitXL Workspace in ROS Melodic ------------ \033[0m "
echo -e "\033[42m ---------- Systemupdates werden ausgefuehrt - Passwort erforderlich  ------------ \033[0m "

sudo apt update
sudo apt dist-upgrade -y

cd ~/catkin_ws/src/

echo -e "\033[42m ---------- Installation der noetigen ROS-Pakete  ------------ \033[0m "
sudo apt install ros-melodic-navigation -y
sudo apt install ros-melodic-robot-localization -y
sudo apt install ros-melodic-mavros-* -y
sudo apt install ros-melodic-gmapping -y
sudo apt install ros-melodic-teb-local-planner -y
sudo apt install ros-melodic-nmea-navsat-driver -y
sudo apt install ros-melodic-twist-mux -y
sudo apt install ros-melodic-gazebo-ros-control -y
sudo apt install ros-melodic-teleop-twist-keyboard -y
sudo apt install ros-melodic-tf2-sensor-msgs -y
sudo apt install ros-melodic-velocity-controllers -y
sudo apt install ros-melodic-urg-node -y
sudo apt install ros-melodic-depthimage-to-laserscan -y
sudo apt install ros-melodic-ira_laser_tools -y
sudo apt install ros-melodic-rgbd-launch ros-melodic-libuvc ros-melodic-libuvc-camera ros-melodic-libuvc-ros -y
sudo apt install libsdl-image1.2-dev libsdl1.2-dev
sudp apt install ros-melodic-robotnik-base-hw-lib ros-melodic-robotnik-msgs
#sudo apt install ros-melodic-summit-xl-robot-control -y //Not avialable

git clone https://github.com/RobotnikAutomation/summit_xl_sim
git clone https://github.com/GeraldHebinck/summit_xl_common
git clone https://github.com/GeraldHebinck/robotnik_sensors
git clone https://github.com/RobotnikAutomation/robotnik_base_hw.git -b melodic-devel
git clone https://github.com/rst-tu-dortmund/costmap_prohibition_layer.git
git clone https://github.com/ros-geographic-info/geographic_info.git
git clone https://github.com/ros-geographic-info/unique_identifier.git
git clone https://github.com/orbbec/ros_astra_camera
git clone https://github.com/orbbec/ros_astra_launch
git clone https://github.com/alin185/whs_summit
git clone https://github.com/GeraldHebinck/summit_xl_controller

echo -e "\033[42m ---------- Aktualisiere alle Abhaengigkeiten der ROS-Pakete ---------- \033[0m"
source ~/.bashrc
rosdep update
rosdep install --from-paths . --ignore-src -r -y

echo -e "\033[42m ---------- Ausfuehren von catkin build ---------- \033[0m"
cd ~/catkin_ws/
catkin build

echo -e "\033[42m ---------- SummitXL Workspace ist installiert - have fun! ----------   \033[0m"
