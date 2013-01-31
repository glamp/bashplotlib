from distutils.core import setup
from setuptools import find_packages

setup(
    name="bashplotlib",
    version="0.3.3",
    author="Greg Lamp",
    author_email="lamp.greg@gmail.com",
    url="https://github.com/glamp/bashplotlib",
    license=open("LICENSE.txt").read(),
    packages=find_packages(),
    description="plotting from the command line",
    long_description=open("README.txt").read(),
)

