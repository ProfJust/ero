# Basiert auf ROS_Melodic_Installation_auf_Remote_PC.sh
# von OJ fuer robotik.bocholt@w-hs.de
# ROS auf einem Rechner mit Ubuntu Focal 20.04 installieren
# EMR SS2020 Hebinck, Heid

#!/bin/bash
echo -e "\033[1;92m ---------- Skript zur Installation von ROS Noetic auf Ubuntu 20.04  ------------ \033[0m "

echo -e "\033[42m ---------- Systemupdates werden ausgefuehrt - Passwort erforderlich  ------------ \033[0m "
sudo apt update
sudo apt-get dist-upgrade -y
sudo apt install -y git 
 
echo -e "\033[42m ---------- Installiere ROS-Noetic  http://wiki.ros.org/noetic/Installation/Ubuntu  ------------ \033[0m "
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install -y ros-noetic-desktop-full

echo -e "\033[42m ---------- Erstelle catkin_ws  ------------ \033[0m "
mkdir -p ~/catkin_ws/src
mkdir -p ~/catkin_ws/devel
touch ~/catkin_ws/devel/setup.bash

echo -e "\033[42m ---------- Konfiguriere .bashrc ------------ \033[0m "
echo "### ROS - Umgebungsvariablen ###" >> ~/.bashrc
echo "export LC_NUMERIC="en_US.UTF-8"" >> ~/.bashrc
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
echo "export ROS_PACKAGE_PATH=~/catkin_ws/src:/opt/ros/noetic/share" >> ~/.bashrc
echo "## Damit eine Netzwerkkommunikation möglich ist, IP-Adressen einstellen! ##" >> ~/.bashrc
echo "## IP des PCs auf dem der Master laeuft ## " >> .bashrc
echo "export ROS_MASTER_URI=http://localhost:11311" >> ~/.bashrc
echo "# export ROS_MASTER_URI=http://192.168.0.40:11311" >> ~/.bashrc
echo "## IP dieses Rechners " >> .bashrc
echo "export ROS_HOSTNAME=127.0.0.1" >> ~/.bashrc
echo "# export ROS_HOSTNAME=192.168.0.40" >> ~/.bashrc
echo "### Ende ROS - Umgebungsvariablen ###" >> ~/.bashrc
source ~/.bashrc # Damit source funktioniert, muss das Skript mit Bash und nicht mit SH ausgefuehrt werden

echo -e "\033[42m ---------- Installiere Dependencies und Buildtools ------------ \033[0m "
sudo apt install -y python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
sudo rosdep init
rosdep update

echo -e "\033[42m ---------- Installation beendet ------------ \033[0m "


