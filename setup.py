import os
from setuptools import find_packages, setup


try:
    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
        README = readme.read()
except Exception:
    README = '<failed to open README.md>'


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='gae-app-settings',
    version='1.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Provides a key/value store in Google App Engine for sensitive data.',
    long_description=README,
    url='https://github.com/seawolf42/gae-app-settings',
    author='jeffrey k eliasen',
    author_email='jeff+gae-app-settings@jke.net',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    keywords='',
    install_requires=(),
    tests_require=(),
)
