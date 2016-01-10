# -*- coding: utf-8 -*-
# pelican-blog (c) Ian Dennis Miller

from setuptools import setup
import os

version = '0.1'


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


setup(
    version=version,
    name='pelican-blog',
    description="A blog based upon Pelican",
    packages=[
    ],
    scripts=[
        "bin/new-blog.sh",
    ],
    long_description="""A blog based upon Pelican""",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    include_package_data=True,
    keywords='',
    author="Ian Dennis Miller",
    author_email="ian@iandennismiller.com",
    url='http://iandennismiller.com',
    install_requires=read('requirements.txt'),
    license='MIT',
    zip_safe=False,
)
