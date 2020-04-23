#!/usr/bin/env python 
import os
from setuptools import find_packages, setup 

project = "pysegyutils"
version = "0.0.1"

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    long_description = readme.read()

setup(
    name=project,
    version=version, 
    description="pysegyutils: Utilities for manipulating SEGY files",
    long_description=long_description, 
    author="TGS",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    keywords="floyd",
    install_requires=[
        "click>=6.7,<7",
        "scandir;python_version<'3.5'",
        "segyio==1.9.1",
    ],
    setup_requires=[],
    dependency_links=[],
    entry_points={
        "console_scripts": [
            "pysegyutils = pysegyutils.main:cli",
        ],
    },
    tests_require=[
        "pytest",
    ],
)
