from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

from launch.substitutions import Command, PathJoinSubstitution


def generate_launch_description():

    # Path to robot xacro
    robot_description_path = PathJoinSubstitution([
        FindPackageShare("my_robot_description"),
        "urdf",
        "my_robot.urdf.xacro"
    ])

    robot_description = {
        "robot_description": Command(["xacro ", robot_description_path])
    }

    # Start Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare("ros_gz_sim"),
                "launch",
                "gz_sim.launch.py"
            ])
        ),
        launch_arguments={
            "gz_args": "empty.sdf -r --render-engine ogre"
        }.items()
    )

    # Robot State Publisher
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[robot_description]
    )

    # Spawn robot in Gazebo
    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        output="screen",
        arguments=[
            "-topic", "robot_description",
            "-name", "my_robot"
        ]
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_robot
    ])