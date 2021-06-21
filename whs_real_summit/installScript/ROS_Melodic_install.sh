# Basiert auf ROS_Melodic_Installation_auf_Remote_PC.sh
# von OJ fuer robotik.bocholt@w-hs.de
# ROS auf einem Rechner mit Ubuntu Bionic 18.04 installieren
# SS2020 Hebinck, Heid

#!/bin/bash
echo -e "\033[1;92m ---------- Skript zur Installation von ROS Melodic auf Ubuntu 18.04  ------------ \033[0m "

echo -e "\033[42m ---------- Systemupdates werden ausgefuehrt - Passwort erforderlich  ------------ \033[0m "
sudo apt update
sudo apt dist-upgrade -y
sudo apt install git -y
sudo apt install openssh-server -y

echo -e "\033[42m ---------- Installiere ROS-Melodic  http://wiki.ros.org/melodic/Installation/Ubuntu  ------------ \033[0m "
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-melodic-desktop-full -y


echo -e "\033[42m ---------- Erstelle catkin_ws  ------------ \033[0m "
mkdir -p ~/catkin_ws/src
mkdir -p ~/catkin_ws/devel
touch ~/catkin_ws/devel/setup.bash

echo -e "\033[42m ---------- Konfiguriere .bashrc ------------ \033[0m "
echo "### ROS - Umgebungsvariablen ###" >> ~/.bashrc
echo "export LC_NUMERIC="en_US.UTF-8"" >> ~/.bashrc
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
echo "export ROS_PACKAGE_PATH=~/catkin_ws/src:/opt/ros/melodic/share" >> ~/.bashrc
echo "## Damit eine Netzwerkkommunikation möglich ist, IP-Adressen einstellen! ##" >> ~/.bashrc
echo "## IP des PCs auf dem der Master laeuft ## " >> .bashrc
echo "export ROS_MASTER_URI=http://localhost:11311" >> ~/.bashrc
echo "#export ROS_MASTER_URI=http://summit-180110A:11311/" >> ~/.bashrc
echo "## IP dieses Rechners " >> .bashrc
echo "export ROS_HOSTNAME=127.0.0.1" >> ~/.bashrc
echo "#export ROS_HOSTNAME=summit-180110A" >> ~/.bashrc
echo "### Ende ROS - Umgebungsvariablen ###" >> ~/.bashrc
source ~/.bashrc

echo -e "\033[42m ---------- Dependencies for building packages ------------ \033[0m "
sudo apt install python-catkin-tools python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential -y
sudo rosdep init
rosdep update

cd ~/catkin_ws
catkin init

echo -e "\033[42m ---------- Installation beendet ------------ \033[0m "
