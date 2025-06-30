from setuptools import find_packages, setup
import os               # Added
from glob import glob   # Added

package_name = 'tf_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name + '/launch', glob('launch/*.py')),     # Added
        ('share/' + package_name + '/rviz', glob('rviz/*.rviz')),       # Added
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dev',
    maintainer_email='tom.birchler@hotmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Add the two entry points for the static and dynamic TF publishers
            # Structure: 'name_of_script = package_name.module_name:function_name'
            # How to run the script: ros2 run tf_demo name_of_script
            
        ],
    },
)
