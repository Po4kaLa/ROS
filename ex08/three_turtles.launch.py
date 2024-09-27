from launch import LaunchDescription  
from launch_ros.actions import Node  
  
def generate_launch_description():  
    return LaunchDescription([  
        Node(  
            package='turtlesim',  
            namespace='turtlesim1',  
            executable='turtlesim_node',
            arguments=['--ros-args', '--log-level', 'WARN'],  
            name='sim'  
        ),  
        Node(  
            package='turtlesim',  
            namespace='turtlesim2',  
            executable='turtlesim_node',
            arguments=['--ros-args', '--log-level', 'WARN'],
            name='sim'  
        ),  
        Node(  
            package='turtlesim',  
            namespace='turtlesim3',  
            executable='turtlesim_node',
            arguments=['--ros-args', '--log-level', 'WARN'],  
            name='sim'  
        ),  
        Node(  
            package='turtlesim',  
            executable='mimic',  
            name='mimic_turtle2',  
            remappings=[  
                ('/input/pose', '/turtlesim1/turtle1/pose'),  
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),  
            ]  
        ), 
        Node(  
            package='turtlesim',  
            executable='mimic',  
            name='mimic_turtle3',  
            remappings=[  
                ('/input/pose', '/turtlesim2/turtle1/pose'),  
                ('/output/cmd_vel', '/turtlesim3/turtle1/cmd_vel'),  
            ]  
        )
    ])

# Не работает управление с клавиатуры:
# ros2 run turtlesim turtle_teleop_key --ros-args -r /output/cmd_vel:=/turtlesim1/turtle1/cmd_vel
# Управление только через публикацию в топик: 
# ros2 topic pub -r 1 /turtlesim1/turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}"