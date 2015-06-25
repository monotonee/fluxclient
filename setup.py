#!/usr/bin/env python

from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext
import platform
import sys
import os

from fluxclient import VERSION as _VERSION

if not sys.version_info >= (3, 3):
    print("ERROR: fluxclient require Python version grather then 3.3\n")
    sys.exit(1)

os.chdir(os.path.abspath(os.path.dirname(__file__)))

VERSION = ".".join([str(i) for i in _VERSION])

install_requires = ['setuptools', 'pycrypto', 'pyserial', 'pillow']

setup(
    name="fluxclient",
    version=VERSION,
    author="Flux Crop.",
    author_email="cerberus@flux3dp.com",
    description="",
    license="?",
    packages=find_packages(),
    test_suite="tests.main.everything",
    entry_points={
        "console_scripts": [
            "flux_discover=fluxclient.commands.discover:main",
            "flux_passwd=fluxclient.commands.passwd:main",
            "flux_auth=fluxclient.commands.auth:main",
            "flux_config_network=fluxclient.commands.config_network:main",
            "flux_robot=fluxclient.commands.robot:main",
            "flux_scan=fluxclient.commands.scan:main",
            "flux_usb=fluxclient.commands.usb:main",

            "flux_laser=fluxclient.commands.laser_patten:main"
        ],
    },
    install_requires=install_requires,
    cmdclass = {'build_ext': build_ext},
    ext_modules=[
        # Extension(
        #     'fluxclient.robot.aes_socket', sources=[
        #         "src/robot/aes_socket.pyx"],
        #     extra_compile_args=["-std=c99"],
        #     libraries=[],
        #     extra_objects=[], include_dirs=[])
    ]
)
