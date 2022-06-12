#!/usr/bin/env python
from setuptools import setup
import os

req_modules = []

setup(
    name='proxmox-utils',
    author='Sitrox',
    maintainer='Sitrox',
    version='0.0.1',
    url='https://github.com/sitrox/proxmox-utils',
    py_modules=[],
    download_url='https://github.com/sitrox/proxmox-utils/tree',
    packages=['proxmox_utils'],
    scripts=['bin/kvm-activate-template', 'bin/kvm-clone', 'bin/kvm-create-template', 'bin/kvm-list-templates', 'bin/kvm-remove'],
    description='Useful shell (python) scripts for managing proxmox virtual environment',
    install_requires = req_modules,
    entry_points = {
        #'console_scripts': ['ccss = clevercss.ccss:main']
    },
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
    #test_suite = 'tests.all_tests',
)
