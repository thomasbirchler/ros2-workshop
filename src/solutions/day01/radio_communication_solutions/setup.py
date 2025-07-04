from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'radio_communication_solutions'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'srv'), glob('srv/*.srv')),
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
            'radio_broadcaster_sol = radio_communication_solutions.radio_broadcaster_sol:main',
            'radio_listener_sol = radio_communication_solutions.radio_listener_sol:main',
            'get_now_playing_service_sol = radio_communication_solutions.get_now_playing_service_sol:main',
        ],
    },
)
