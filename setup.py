#!/usr/bin/env python

from setuptools import setup

import base32_crockford


setup(
    name='base32-crockford',
    version='0.3.0',
    description=("A Python implementation of Douglas Crockford's "
                 "base32 encoding scheme"),
    long_description=base32_crockford.__doc__,
    license='BSD',
    author='Jason Bittel',
    author_email='jason.bittel@gmail.com',
    url='https://github.com/jbittel/base32-crockford',
    download_url='https://pypi.python.org/pypi/base32-crockford/',
    py_modules=['base32_crockford'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
