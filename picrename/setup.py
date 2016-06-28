#!/usr/bin/env python

from setuptools import setup

setup(
        name="picrename",
        version="0.2.0",
        description="Rename pictures with a datestring and incrementing index",
        entry_points={
            "console_scripts": [
                "picrename = picrename:main"
                ]
            },
        classifiers=[
            "Natural Language :: English",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 2.7"
            ],
        author="Nikolai Schlegel",
        packages=["picrename", "picrename.prnm"],
        install_requires=[
            ])

