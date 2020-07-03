import re
from setuptools import setup, find_packages


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Mopidy-Amp-Control',
    version=get_version('mopidy_amp_control/__init__.py'),
    url='https://github.com/N-kay/mopidy-amp-control',
    license='Apache License, Version 2.0',
    author='N-kay',
    author_email='n.kay01@gmail..com',
    description='Runs configurable commands to power / unpower your amplifier. Requires pre-built functionality to do that, this just runs the commands at appropriat etimes.',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 0.14',
        'Pykka >= 1.1',
    ],
    entry_points={
        'mopidy.ext': [
            'amp_control = mopidy_amp_control:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
