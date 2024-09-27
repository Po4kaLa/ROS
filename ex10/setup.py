from setuptools import setup

package_name = 'ex10'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pochka',
    maintainer_email='sashaokunev23@gmail.com',
    description='A ROS2 package for converting text commands to cmd_vel for turtlesim.',
    license='License declaration',
    tests_require=['pytest'],
    entry_points={
       'console_scripts': [
           'text_to_cmd_vel = ex10.text_to_cmd_vel:main',
       ],
   },
)