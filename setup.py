from setuptools import find_packages, setup

setup(
    name="w3utils",
    version="0.0.2",
    author="thegismar",
    description="Some convenience functions to make web3 coding easier.",
    packages=find_packages(),
    install_requires=[pandas],
    python_requires='>=3.6',
)