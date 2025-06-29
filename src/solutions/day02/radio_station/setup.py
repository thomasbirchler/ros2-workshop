from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'radio_station'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'srv'),
        glob('srv/*.srv')),
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
            'service_server = radio_station.get_now_playing_server:main',
            'service_client = radio_station.get_now_playing_client:main',
            'radio_dj = radio_station.action_server_node:main',
            'song_requester = radio_station.action_client_node:main',
        ],
    },
)
