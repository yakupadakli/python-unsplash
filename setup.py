#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name="python-unsplash",
    version="1.2.1",
    description="A Python client for the Unsplash API.",
    license="MIT",
    author="Yakup Adaklı",
    author_email="yakup.adakli@gmail.com",
    url="http://github.com/yakupadakli/python-unsplash.git",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "oauthlib>=2.0.1",
        "requests>=2.31.0",
        "requests-oauthlib>=0.7.0",
        "six>=1.10.0",
    ],
    keywords="unsplash library",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.11",
    ],
    zip_safe=True,
)
