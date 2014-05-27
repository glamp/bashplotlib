#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="bashplotlib",
    version="0.6.1",
    author="Greg Lamp",
    author_email="lamp.greg@gmail.com",
    url="https://github.com/glamp/bashplotlib",
    license="BSD",
    packages=find_packages(),
    description="plotting in the terminal",
    long_description=open("README.rst").read(),
    entry_points = {
        'console_scripts': [
            'hist=bashplotlib.histogram:main',
            'scatter=bashplotlib.scatterplot:main',
        ]
    }
)

