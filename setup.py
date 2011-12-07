#!/usr/bin/env python
from setuptools import setup
import os

fp = open(os.path.join(os.path.dirname(__file__), "README.rst"))
readme_text = fp.read()
fp.close()

req_modules = []

setup(
    name='proxmox-utils',
    author='Remo Fritzsche',
    author_email='dev@remofritzsche.com',
    maintainer='Remo Fritzsche',
    maintainer_email='dev@remofritzsche.com',
    version='0.0.1',
    url='https://github.com/remofritzsche/proxmox-utils',
    py_modules=[],
    download_url='https://github.com/remofritzsche/proxmox-utils/tree',
    packages=['proxmox_utils'],
    scripts=['bin/kvm-activate-template', 'bin/kvm-clone', 'bin/kvm-create-template', 'bin/kvm-list-templates', 'bin/kvm-remove'],
    description='Useful shell (python) scripts for managing proxmox virtual environment',
    long_description=readme_text,
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
