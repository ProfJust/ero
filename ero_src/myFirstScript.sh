#!/bin/bash
# My first script

echo "Hello World!"

echo "Shellskript zur Installation der SummitXL-Pakete" 

sudo apt-get dist-upgrade
pwd
cd ~/catkin_ws/src/

mkdir -p ero_src

print("Installiert die Summit-Pakete")

git clone https://github.com/RobotnikAutomation/summit_xl_sim
git clone https://github.com/RobotnikAutomation/summit_xl_common
git clone https://github.com/RobotnikAutomation/robotnik_msgs
git clone https://github.com/RobotnikAutomation/robotnik_sensors