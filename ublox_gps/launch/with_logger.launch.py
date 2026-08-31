from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    ublox_gps_dir = get_package_share_directory('ublox_gps')
    gps_logger_dir = get_package_share_directory('gps_logger_v2')

    base_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ublox_gps_dir, 'launch', 'ublox_gps_node_base-launch.py')
        )
    )

    rover_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ublox_gps_dir, 'launch', 'ublox_gps_node_rover-launch.py')
        )
    )

    gps_logger_node = Node(
        package='gps_logger_v2',
        executable='gps_saver_node',
        name='gps_logger_node',
        output='screen'
    )

    return LaunchDescription([
        base_launch,
        rover_launch,
        gps_logger_node
    ])

