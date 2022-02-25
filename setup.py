#!/usr/bin/env python
import setuptools

setuptools.setup(
    name="hydro_cruncher",
    version="0.1.0",
    author="Pascal Horton",
    author_email="pascal.horton@giub.unibe.ch",
    package_dir={"hydro_cruncher": "hydro_cruncher"},
    packages=setuptools.find_packages(where="hydro_cruncher"),
    entry_points={"console_scripts": ["hydro-cruncher=hydro_cruncher.__main__:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Pytest"
    ],
)