#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.rst") as fh:
    long_description = fh.read()

setup(
    name="bashplotlib",
    version="0.6.5",
    author="Greg Lamp",
    author_email="lamp.greg@gmail.com",
    url="https://github.com/glamp/bashplotlib",
    license="BSD",
    packages=find_packages(),
    description="plotting in the terminal",
    long_description=long_description,
    entry_points = {
        'console_scripts': [
            'hist=bashplotlib.histogram:main',
            'scatter=bashplotlib.scatterplot:main',
        ]
    },
    keywords=['plotting', 'console', 'shell'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)

