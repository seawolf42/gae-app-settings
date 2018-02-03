import os
import subprocess
import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


install_dependencies = ()

setup(
    name='XXX',
    version='XXX',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='XXX',
    long_description=README,
    url='https://github.com/seawolf42/XXX',
    author='jeffrey k eliasen',
    author_email='jeff+XXX@jke.net',
    classifiers=(
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: XXX',
    ),
    keywords='',
    install_requires=install_dependencies,
    tests_require=install_dependencies + (),
)
