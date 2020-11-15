# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from py_commons import __version__


def _get_install_requires():
    with open("requirements.txt") as f:
        lines = f.readlines()
        return list(map(lambda s: s.strip(), lines))


name = "py_commons"
setup(
    name=name,
    version=__version__,
    keywords=["pip", "commons", "common", "utils", "util"],
    description="Common utils for python",
    packages=find_packages(include=[name, f"{name}.*"], exclude=["test", "test.*"]),
    include_package_data=True,
    platforms="any",
    install_requires=_get_install_requires()
)
