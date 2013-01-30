from distutils.core import setup
from setuptools import find_packages

setup(
    name="bashplotlib",
    version="0.2.0",
    packages=find_packages(),
    license=open("LICENSE").read(),
    long_description=open("README.md").read(),
)

