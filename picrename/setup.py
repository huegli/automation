#!/usr/bin/env python

from setuptools import setup

setup(
        name="picrename"
        version="0.1"
        description="Rename pictures with a datestring and incrementing index"
        entry_points={
            "console_scripts": [
                "renamepic = renamepic.renamepic_cli:run"
                ]
            }
        classifiers=[
            "Natural Language :: English",
            "Programming Language :: Python :: 2.7",
        author="Nikolai Schlegel"
        packages=["renamepic", "renamepic.prnm"]
        install_requires=[
            ])

