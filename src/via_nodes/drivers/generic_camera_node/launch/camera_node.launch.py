import launch
import os
from launch import LaunchDescription
from launch_ros.actions import Node

from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    ld = LaunchDescription()
    config = os.path.join(
        get_package_share_directory('generic_camera_driver_node'),
        'config',
        'params.yaml'
    )

    node = Node(
        package='generic_camera_node',
        executable='generic_camera_node',
        name='generic_camera_node',
        namespace='/camera',
        parameters=[
                config
        ]
    )
    ld.add_action(node)

    return ld
