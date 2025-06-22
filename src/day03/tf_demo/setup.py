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
            'static_tf_pub = tf_demo.static_tf_pub:main',
            'dynamic_tf_pub = tf_demo.dynamic_tf_pub:main',
        ],
    },
)
