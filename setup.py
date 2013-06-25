
#!/usr/bin/env python

from setuptools import setup, find_packages

name = "guesslanguage"

setup(
    name = name,
    version = "0.2.1",
    url = "http://silpa.org.in/Guess_Language",
    license = "LGPL-3.0",
    description = "Guess primary language of given text",
    author = "Santhosh Thottingal",
    author_email = "santhosh.thottingal@gmail.com",
    long_description = """Guess the language of given text.Even
    works for text containing multiple languages""",
    packages = find_packages(),
    include_package_data = True,
    setup_requires = ['setuptools-git'],
    install_requires = ['setuptools','silpa_common'],
    zip_safe = False,
    )
