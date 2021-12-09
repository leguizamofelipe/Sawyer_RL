#!/bin/bash 


echo "Starting up Sawyer Gazebo"
gnome-terminal -- cd ros_ws
gnome-terminal -- ./intera.sh sim
gnome-terminal -- roslaunch sawyer_gazebo sawyer_world.launch

