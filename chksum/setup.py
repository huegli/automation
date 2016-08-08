#!/usr/bin/env python

from setuptools import setup

setup(
        name="chksum",
        version="0.0.1",
        description="RUsing SHA256 to calculate a checksum for one or more files",
        entry_points={
            "console_scripts": [
                "chksum = chksum:main"
                ]
            },
        classifiers=[
            "Natural Language :: English",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 2.7"
            ],
        author="Nikolai Schlegel",
        packages=["chksum"],
        install_requires=[],
        test_suite = 'nose.collector',
        test_requires=["nosetests"]
)

