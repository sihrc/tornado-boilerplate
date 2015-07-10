"""
SkyNetServer setup
For development:
    `python setup.py develop`
"""
from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name = "indicoapi"
        packages = find_packages(),
        version = "0.1.0",
    )
