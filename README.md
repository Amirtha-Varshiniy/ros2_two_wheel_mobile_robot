# ROS 2 Two Wheel Mobile Robot 🤖

A two-wheel differential drive mobile robot developed using **ROS 2 Jazzy** and **Gazebo Sim**. This project demonstrates robot modeling with URDF/Xacro, simulation in Gazebo, and visualization in RViz using ROS 2.

---

## Project Overview

This project implements a custom differential drive mobile robot using ROS 2. The robot model is built with **URDF/Xacro** and integrated with **Gazebo Sim** for simulation and **RViz** for visualization.

### Features

- Differential drive mobile robot
- Robot modeling using URDF/Xacro
- Gazebo simulation
- RViz visualization
- ROS 2 launch system
- ROS-Gazebo bridge integration
- Modular robot description

---

## Technologies Used

- ROS 2 Jazzy Jalisco
- Gazebo Sim
- RViz2
- URDF
- Xacro
- XML Launch Files
- CMake
- Ubuntu 24.04

---

## Workspace Structure

```text
my_robot_ws
│
├── build/
├── install/
├── log/
│
└── src
    │
    ├── my_robot_bringup
    │   │
    │   ├── config
    │   │   └── gazebo_bridge.yaml
    │   │
    │   ├── launch
    │   │   └── my_robot.launch.xml
    │   │
    │   ├── CMakeLists.txt
    │   └── package.xml
    │
    └── my_robot_description
        │
        ├── launch
        │   ├── display.launch.xml
        │   └── gazebo.launch.xml
        │
        ├── rviz
        │   └── urdf_config.rviz
        │
        ├── urdf
        │   ├── common_properties.xacro
        │   ├── gazebo.xacro
        │   ├── mobile_base.xacro
        │   └── my_robot.urdf.xacro
        │
        ├── .gitignore
        ├── CMakeLists.txt
        └── package.xml
```

> **Note:** The `build`, `install`, and `log` directories are generated automatically by `colcon build` and are not included in this repository.

---

# Packages

## my_robot_description

Contains:

- URDF/Xacro robot model
- RViz configuration
- Robot visualization launch files

### Folder Structure

```text
my_robot_description
│
├── launch
│   ├── display.launch.xml
│   └── gazebo.launch.xml
│
├── rviz
│   └── urdf_config.rviz
│
├── urdf
│   ├── common_properties.xacro
│   ├── gazebo.xacro
│   ├── mobile_base.xacro
│   └── my_robot.urdf.xacro
│
├── CMakeLists.txt
└── package.xml
```

---

## my_robot_bringup

Contains:

- Main robot launch file
- Gazebo bridge configuration
- Simulation startup files

### Folder Structure

```text
my_robot_bringup
│
├── config
│   └── gazebo_bridge.yaml
│
├── launch
│   └── my_robot.launch.xml
│
├── CMakeLists.txt
└── package.xml
```

---

# Installation

Clone the repository into your ROS 2 workspace:

```bash
cd ~/my_robot_ws/src
git clone <repository-url>
```

Navigate to the workspace:

```bash
cd ~/my_robot_ws
```

Install dependencies:

```bash
rosdep install --from-paths src --ignore-src -r -y
```

Build the workspace:

```bash
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

---

# Running the Robot Simulation

Launch the complete robot simulation:

```bash
ros2 launch my_robot_bringup my_robot.launch.xml
```

This launch file starts:

- Robot State Publisher
- Gazebo Simulation
- Robot Spawn
- ROS-Gazebo Bridge
- Required ROS 2 nodes

---

# Viewing the Robot in RViz

To visualize the robot model:

```bash
ros2 launch my_robot_description display.launch.xml
```

---

# Robot Description

The robot is built using modular Xacro files:

```text
urdf
├── common_properties.xacro
├── gazebo.xacro
├── mobile_base.xacro
└── my_robot.urdf.xacro
```

These files define:

- Robot chassis
- Wheels
- Links and joints
- Physical properties
- Gazebo plugins
- Robot assembly

---

# Future Improvements

- Add LiDAR sensor
- Add RGB-D camera
- Integrate Nav2
- Implement SLAM
- Add autonomous navigation
- Interface with real robot hardware

---

# License

This project is open-source and intended for learning, educational, and research purposes.
