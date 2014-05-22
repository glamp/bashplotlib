#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="bashplotlib",
    version="0.5.3",
    author="Greg Lamp",
    author_email="lamp.greg@gmail.com",
    url="https://github.com/glamp/bashplotlib",
    license=open("LICENSE.txt").read(),
    packages=find_packages(),
    description="plotting in the terminal",
    long_description=open("README.md").read(),
    entry_points = {
        'console_scripts': [
            'hist=bashplotlib.histogram:main',
            'scatter=bashplotlib.scatterplot:main',
        ]
    }
)

