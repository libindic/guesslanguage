#!/usr/bin/env python

from setuptools import setup, find_packages

name = "guesslanguage"

setup(
    name = name,
    version = "0.1",
    url = "http://silpa.org.in/Guess_Language",
    license = "LGPL-3.0",
    description = "Language Guessing library",
    author = "Santhosh Thottingal",
    author_email = "santhosh.thottingal@gmail.com",
    long_description = "This library helps in detecting \
language of given string or text.",
    packages = find_packages('.'),
    package_data = {'.':['guesslanguage/trigrams',
                         'guesslanguage/Blocks.txt']},
    include_package_data = True,
    setup_requires = ['setuptools-git'],
    install_requires = ['setuptools'],
    zip_safe = False,
    )
