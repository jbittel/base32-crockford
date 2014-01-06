#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import base32_crockford


package_data = {
    '': ['LICENSE', 'README.rst'],
}

setup(
    name='base32-crockford',
    version='0.1.0',
    description=("A Python implementation of Douglas Crockford's "
                 "base32 encoding scheme"),
    long_description=base32_crockford.__doc__,
    license='BSD',
    author='Jason Bittel',
    author_email='jason.bittel@gmail.com',
    url='https://github.com/jbittel/base32-crockford',
    download_url='https://github.com/jbittel/base32-crockford/downloads',
    py_modules=['base32_crockford'],
    package_data=package_data,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
