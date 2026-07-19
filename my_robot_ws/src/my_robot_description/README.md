# ROS 2 Two Wheel Mobile Robot

A two-wheel differential drive mobile robot developed using ROS 2 and Gazebo simulation.  
This project includes the robot description (URDF/Xacro), launch files, and simulation setup required to visualize and control the robot.

## Project Overview

This project implements a custom two-wheel mobile robot in ROS 2. The robot model is created using URDF/Xacro and can be simulated in Gazebo with ROS 2 integration.

The project demonstrates:
- Robot modeling using URDF/Xacro
- ROS 2 package creation
- Robot visualization in RViz
- Gazebo simulation
- Differential drive mobile robot configuration
- ROS 2 launch system

## Software Requirements

- Ubuntu 24.04
- ROS 2 Jazzy Jalisco
- Gazebo Harmonic
- RViz2
- colcon build tools

## Package Structure

my_robot_ws
│
├── build/
├── install/
├── log/
│
└── src
│
├── my_robot_bringup
│ │
│ ├── config
│ │ └── gazebo_bridge.yaml
│ │
│ ├── launch
│ │ └── my_robot.launch.xml
│ │
│ ├── CMakeLists.txt
│ └── package.xml
│
│
└── my_robot_description
│
├── launch
│ ├── display.launch.xml
│ └── gazebo.launch.xml
│
├── rviz
│ └── urdf_config.rviz
│
├── urdf
│ ├── common_properties.xacro
│ ├── gazebo.xacro
│ ├── mobile_base.xacro
│ └── my_robot.urdf.xacro
│
├── .gitignore
├── CMakeLists.txt
└── package.xml

# Build
'''bash
cd ~/my_robot_ws
colcon build
source install/setup.bash

To launch the complete robot simulation in Gazebo:
ros2 launch my_robot_bringup my_robot.launch.xml

To visualize the robot model in RViz:
ros2 launch my_robot_description display.launch.xml

# Packages
## my_robot_description

Contains:
- URDF/Xacro robot model
- RViz configuration
- Robot visualization launch files

## my_robot_bringup

Contains:
- Main robot launch file
- Gazebo bridge configuration
- Simulation startup files
