"""
setup module for prog_rock
"""

from __future__ import (absolute_import, unicode_literals)
from os.path import dirname, join, realpath
from setuptools import setup, find_packages
from sys import version_info


cwd = dirname(realpath(__file__))
with open(join(cwd, 'prog_rock/version.py')) as version_file:
    for line in version_file:
        if line.startswith('__version_info__'):
            exec(line)


long_description = ('')


requirements = [

]


setup(
    name='prog_rock',
    version='.'.join([str(ver) for ver in __version_info__]),
    description=(''),
    long_description=long_description,
    url='https://www.github.com/ihiji/prog_rock',
    author='Matthew Planchard',
    author_email='mplanchard@ihiji.com',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Development Status :: 2 - Pre-Alpha',
        'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        'Development Status :: 6 - Mature',
        'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Version Control',
        'Topic :: System :: Software Distribution',
        'Topic :: Utilities',
    ],
    keywords=(''),
    packages=find_packages(exclude=['tests']),
    install_requires=requirements,
)
