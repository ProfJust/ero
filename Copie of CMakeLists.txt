cmake_minimum_required(VERSION 2.8.3)
project(ero)

### by OJ for ero 30.4.2020

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  message_generation
  rospy
)

#add_message_files(
#  FILES  Twist.msg   # e.g. Floats.msg HeaderString.msg
#)
#add_service_files(
#  DIRECTORY srv 
#  FILES AddTwoInts.srv BadTwoInts.srv
#)

## Generate services in the 'srv' folder
# add_service_files(
#  FILES  # e.g. Floats.srv HeaderString.srv
#)

## Generate added messages and services with any dependencies
#generate_messages()

catkin_package(
  CATKIN_DEPENDS message_runtime message_generation rospy
)

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if your package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
#catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES my_pkg
 #  CATKIN_DEPENDS message_generation rospy
#  DEPENDS system_lib
#)

###########
## Build ##
###########

## Uncomment if the package has a setup.py
catkin_python_setup()


####### OJ: hier alle ins ROS einzufuegenden py-Skripte auflisten
####### ! Don't forget to chmod +x filename.py 
####### geht rekursiv fuer alle Unterordner mit (Punkt nicht vergessen)
####### chmod --recursive +x .

catkin_install_python(PROGRAMS 
   bin/ero_v1_sw/bsp01_for.py 
   bin/ero_v1_sw/hello_world.py
   bin/ero_v2_sw/talker.py
   bin/ero_v2_sw/listener.py
   bin/ero_p1_bmi/bmi2.py
   bin/ero_p2_turtle/p2_moveTurtle_distance_VORGABE.py 
   bin/ero_p2_turtle/p2_moveTurtle_distance_LOESUNG.py 
   bin/ero_p3_turtleOOP/p3_TurtleClass_move2goal_VORGABE.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

