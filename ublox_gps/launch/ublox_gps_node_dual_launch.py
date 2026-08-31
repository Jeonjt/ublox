from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription

from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    ublox_gps_launch_dir = get_package_share_directory('ublox_gps')

    base_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(ublox_gps_launch_dir, 'launch', 'ublox_gps_node_base-launch.py'))
    )

    rover_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(ublox_gps_launch_dir, 'launch', 'ublox_gps_node_rover-launch.py'))
    )

    return LaunchDescription([
        base_launch,
        rover_launch
    ])
