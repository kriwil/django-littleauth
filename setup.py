#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='littleauth',
    version='0.3.1',
    description="Custom User model with uuid as primary key, and email as username.",
    long_description=readme + '\n\n' + history,
    author="Aldiantoro Nugroho",
    author_email='kriwil@gmail.com',
    url='https://github.com/kriwil/django-littleauth',
    packages=[
        'littleauth',
    ],
    package_dir={'littleauth':
                 'littleauth'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='littleauth',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
