from setuptools import find_packages, setup

package_name = 'simulation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    ('share/' + package_name + '/launch',
        ['launch/display_firebot.launch.py',
            'launch/spawn_firebot.launch.py']),
    ('share/' + package_name + '/urdf',
        ['urdf/firebot.urdf']),
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='armaan',
    maintainer_email='armaan18032008@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
